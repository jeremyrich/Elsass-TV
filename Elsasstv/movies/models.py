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
    
    
