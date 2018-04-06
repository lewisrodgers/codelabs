# The first item in the recipe defines that we are going to create our Docker
# container based on the default Python 3 Docker image.
# Using lightweight alpine image
FROM python:3.6-alpine

# After that, we update APK and install pipenv.
# Note: We don't need to cache installed files which reduces the size of the
# image (--no-cache-dir).
# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Having pipenv, we define the working directory that we will use in the image, 
# and we copy the code needed to bootstrap and run the application.
# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY hello.py Pipfile Pipfile.lock serve.sh ./

# In the fourth step, we use pipenv to install all our Python dependencies.
# Install API dependencies
RUN pipenv install

# Lastly, we define that our image will communicate through port 5000 and that 
# this image, when executed, needs to run the serve.sh script to start Flask.
# Start app
EXPOSE 5000
ENTRYPOINT [ "/usr/src/app/serve.sh" ]
