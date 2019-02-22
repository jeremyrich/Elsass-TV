# Elsass-TV

Django 2.0 project - Florence Schwartz, Quentin Dufrois, Jérémy Rich

## Installation

### First you need to copy the unzipped folder in the desired directory

### Second you need a running [elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html "elasticsearch") instance on default port: 9200

### Finally deploy a new virtualenv and launch the server
In the terminal:

* Go to the project directory
```
cd path/to/project_folder/
```

* Activate the environment (MacOS/Linux)
```
virtualenv -p python3 djangoenv
cd path/to/djangoenv
source djangoenv/bin/activate
pip3 install -r path/to/requirements.txt
```

* Then run the django server
```
python3 manage.py runserver
```

* Open your web browser and enter the URL displayed in the terminal (http://127.0.0.1:8000/ or http://localhost:8000/).

* Local installation will result in an empty mysql database, if you need a sample database please open an issue. 


## The Application

### Users

You already have 4 users in order to test different features, the users are called *florence*, *quentin*, *jeremy* and *martin*, and they all have the same password, which is *Maman246*.


### Features

With Elsasstv, you can navigate through Movies (TV shows are not yet connected), check out their details, casts, similar shows, etc. Once logged in, you can add movies to your favorites, add friends by typing their username in the invite bar and visualize your friends favorites. The notification button turns red when you have a new friend request.

Now, you can try to consult movies, create your own user and add some movies to your favorites, invite friends and read your notifications. Enjoy !



