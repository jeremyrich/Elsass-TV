"""
Import json data from URL to Datababse
"""
from django.core.management.base import BaseCommand, CommandError
import requests
import json
from movies.models import *
from datetime import datetime
import time
import sys



class Command(BaseCommand):
    def createEntry(self, data):
        try:
            person, created = Person.objects.get_or_create(
                id = data['id'],
                imdb_id = data["imdb_id"],
                name = data['name'],
                gender = data['gender'],
                birthday = data['birthday'],
                deathday = data['deathday'],
                place_of_birth = data['place_of_birth'],
                known_for_department = data['known_for_department'],
                biography = data['biography'],
                popularity = data['popularity'],
                profile_path = data['profile_path'],
            )
            if created:
                person.save()
                display_format = "\nPerson, {}, has been saved."
                print(display_format.format(person))
        except Exception as ex:
            with open('errors_persons.txt', 'a') as errors:
                sys.stdout = errors
                print(str(ex))
                msg = "\n\nSomething went wrong saving this person: {}, id:{} \n{}".format(data['name'], data['id'], str(ex))
                print(msg)
                sys.stdout = sys.__stdout__

    def getIDs(self):
        list_id = []
        with open('person_ids_02_04_2019.json', 'r') as json_data:
            for line in json_data:
                data = json.loads(line)
                list_id.append(data['id'])

        return list_id

    def handle(self, person_id):
        """
        Makes a GET request to the  API.
        """
        response = requests.get(
            url='https://api.themoviedb.org/3/person/'+ str(person_id) + '?api_key=c7ee2bafbeec613e48d032777e99746f',
        )
        data = response.json()

        return self.createEntry(data)

test  = Command()
list_id = test.getIDs()
for i in range(200):
    test.handle(list_id[i])
    if i % 40 == 0 :
        time.sleep(1)
    


