import logging

from google.appengine.ext import ndb
from flask import Flask


app = Flask(__name__)


class Product(ndb.Model):
    uuid = ndb.IntegerProperty()


@app.route('/data')
def create_products():
    records = []

    for i in range(5000):
        product = Product(uuid=i)
        records.append(product)

    logging.info("Number of records to write: {}".format(len(records)))

    ndb.put_multi(records)



@app.route('/delete')
def delete_store():
    records = Product.query().fetch(keys_only=True)

    logging.info("Number of records to delete: {}".format(len(records)))

    ndb.delete_multi(records)



@app.route('/list')
def list_store():
    records = ndb.Query(kind='Product').fetch(keys_only=True)

    logging.info("Number of records to list: {}".format(len(records)))
