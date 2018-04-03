# ref: https://cloud.google.com/community/tutorials/use-cloud-pubsub-cloud-storage-app-engine#html-files

import collections
import json
import logging
import os
import urllib

import cloudstorage
import jinja2
import webapp2
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
import googleapiclient.discovery


THUMBNAIL_BUCKET = 'thumbnails178216'
PHOTO_BUCKET = 'logging-178216.appspot.com'
NUM_NOTIFICATIONS_TO_DISPLAY = 20
MAX_LABELS = 5


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir))

class Notification(ndb.Model):
    message = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    generation = ndb.StringProperty()

class ThumbnailReference(ndb.Model):
    thumbnail_name = ndb.StringProperty()
    thumbnail_key = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    labels = ndb.StringProperty(repeated=True)
    original_photo = ndb.StringProperty()

# get method for getting information from the server and writing it 
# to the home page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        notifications = Notification.query().order(
            -Notification.date).fetch(NUM_NOTIFICATIONS_TO_DISPLAY)
        template_values = {'notifications': notifications}
        template = jinja_environment.get_template('notifications.html')
        self.response.write(template.render(template_values))

class PhotosHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('photos.html')
        self.response.write(template.render(template_values))

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('search.html')
        self.response.write(template.render(template_values))

""" 
Post information to the server.
When you receive Pub/Sub messages, you must get necessary
information from it and acknowledge its reception.

Only executed if the new notification is not a repeat and
is not for an OBJECT_METADATA_UPDATE event
"""
class ReceiveMessage(webapp2.RequestHandler):
    def post(self):
        logging.debug('Post body: {}'.format(self.request.body))
        message = json.loads(urllib.unquote(self.request.body))
        attributes = message['message']['attributes']

        # Acknowledge reception of message
        self.response.status = 204

        event_type = attributes.get('eventType')
        photo_name = attributes.get('objectId')
        generation_number = str(attributes.get('objectGeneration'))
        overwrote_generation = attributes.get('overwroteGeneration')
        overwritten_by_generation = attributes.get('overwrittenByGeneration')

        # Here we can target specific object types that we're interested in.
        try:
            # Finds the index at which '.jpg' starts
            # '.jpg' is found at index 5 given 'hello.jpg'
            index = photo_name.index('.jpg')
        except:
            return

        thumbnail_key = '{}{}{}'.format(
            # Splits the the filename at '.jpg' so we can insert the generation number. 
            # e.g., hello1234.jpg
            photo_name[:index], generation_number, photo_name[index:])

        new_notification = create_notification(
            photo_name,
            event_type,
            generation_number,
            overwrote_generation=overwrote_generation,
            overwritten_by_generation=overwritten_by_generation)

        exists_notification = Notification.query(
            Notification.message == new_notification.message,
            Notification.generation == new_notification.generation).get()

        # If the message already exists in Datastore, do nothing.
        if exists_notification:
            return

        # An event type of OBJECT_METADATA_UPDATE signal no changes to the bucket.
        # No message exists in this case.
        if new_notification.message is None:
            return

        # Ok to store message to Datastore.
        new_notification.put()

        """
        On OBJECT_FINALIZE 
        1. shrink uploaded photo to a thumbnail,
        2. store it in the thumbnail bucket in Storage
        3. label it through the vision API
        3. store reference in Datastore
        """
        if event_type == 'OBJECT_FINALIZE':
            thumbnail = create_thumbnail(photo_name)
            store_thumbnail_in_gcs(thumbnail_key, thumbnail)


def create_notification(photo_name,
                event_type,
                generation,
                overwrote_generation=None,
                overwritten_by_generation=None):
    if event_type == 'OBJECT_FINALIZE':
        if overwrote_generation is not None:
            message = '{} was uploaded and overwrote an older' \
                ' version of itself.'.format(photo_name)
        else:
            message = '{} was uploaded.'.format(photo_name)
    elif event_type == 'OBJECT_ARCHIVE':
        if overwritten_by_generation is not None:
            message = '{} was overwritten by a newer version.'.format(
                photo_name)
        else:
            message = '{} was archived.'.format(photo_name)
    elif event_type == 'OBJECT_DELETE':
        if overwritten_by_generation is not None:
            message = '{} was overwritten by a newer version.'.format(
                photo_name)
        else:
            message = '{} was deleted.'.format(photo_name)
    else:
        message = None

    return Notification(message=message, generation=generation)


def create_thumbnail(photo_name):
    filename = '/gs/{}/{}'.format(PHOTO_BUCKET, photo_name)
    image = images.Image(filename=filename)
    image.resize(width=180, height=200)
    return image.execute_transforms(output_encoding=images.JPEG)


def store_thumbnail_in_gcs(thumbnail_key, thumbnail):
    write_retry_params = cloudstorage.RetryParams(
        backoff_factor=1.1, max_retry_period=15)
    filename = '/{}/{}'.format(THUMBNAIL_BUCKET, thumbnail_key)
    with cloudstorage.open(
            filename, 'w', 
            content_type='image/jpeg', 
            retry_params=write_retry_params) as filehandle:
        filehandle.write(thumbnail)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/photos', PhotosHandler),
    ('/search', SearchHandler),
    ('/_ah/push-handlers/receive_message', ReceiveMessage)
], debug=True)

