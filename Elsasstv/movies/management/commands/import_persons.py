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
from threading import Thread


class APIThreadingRequest(Thread):

    def __init__(self, API_key, min_range, step):

        super().__init__()
       
        self.API_key = API_key
        self.min_range = min_range
        self.step = step

    def run(self):
        print('Thread active...')
        test = Command()
        list_id = test.getIDs()
        for i in range(self.min_range, len(list_id), self.step):
            test.handle(list_id[i], self.API_key)
            
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
                
        except Exception as ex:
            with open('errors_persons.txt', 'a') as errors:                
                errors.write(str(ex))
                errors.write("\n\nSomething went wrong saving this person: {}, id:{} \n{}".format(data['name'], data['id'], str(ex)))
            
               
    def getIDs(self):
        list_id = []
        with open('person_ids_02_04_2019.json', 'r', errors='ignore') as json_data:
            for line in json_data:
                data = json.loads(line)
                list_id.append(data['id'])
        
        In_db_persons = Person.objects.all() 
        list_id_persons = [film.id for film in In_db_persons] 
        list_id = list(set(list_id) - set(list_id_persons))

        return list_id

    def handle(self, person_id, API_key):
        """
        Makes a GET request to the  API.
        """
        while True: # To avoid errors when calling the api more than 40 times in 10 seconds
            response = requests.get(
                url='https://api.themoviedb.org/3/person/'+ str(person_id) + '?api_key=' +str(API_key),
            )
            data = response.json()  
            if 'status_code' in data and data['status_code'] == 25:
                time.sleep(1.0)
            else: 
                break             
   
        return self.createEntry(data)


# We manually split the list of persons in six
thread1 = APIThreadingRequest('94ea7f4f8f9b4ef1f127a421b68e4fc3', 0, 6)
thread2 = APIThreadingRequest('d6c5128f507174794ba9f372ac42e601', 1, 6)
thread3 = APIThreadingRequest('1345cc7cc9f4f819487b0ade825a5ce3', 2, 6)
thread4 = APIThreadingRequest('ebe018b0565f22bd6ac6a02ed6277774', 3, 6)
thread5 = APIThreadingRequest('4b0a1de4dec94d5cccf0e707262474e0', 4, 6)
thread6 = APIThreadingRequest('32dd33a86e1078d2ef32a7ecc9ebe5e4', 5, 6)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()



