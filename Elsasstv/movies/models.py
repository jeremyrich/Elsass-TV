from django.db import models

class Movie(models.Model):

    id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=45)
    original_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)  
    tagline = models.CharField(max_length=200)  
    overview = models.TextField()
    release_date = models.DateTimeField()
    status = models.CharField(max_length=45)
    runtime = models.IntegerField(null=True)
    popularity = models.FloatField(null=True)
    original_langage = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)    
    budget = models.BigIntegerField(null=True)
    revenue = models.BigIntegerField(null=True)   
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    
    
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

    

    
