from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=45)
    name = models.CharField(max_length=200)
    gender = models.IntegerField()
    birthday = models.DateTimeField()
    deathday = models.DateTimeField(null=True)
    place_of_birth = models.CharField(max_length=200)
    known_for_department = models.CharField(max_length=45)
    biography = models.TextField() 
    Popularity = models.FloatField() 
    profile_path = models.CharField(max_length=200)
    
