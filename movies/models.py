from django.db import models
from django.utils import timezone
# Create your models here.
# models has a class Model
class Genre(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Movie(models.Model):
    title=models.CharField(max_length=255)
    release_year=models.IntegerField()
    number_in_stock=models.IntegerField()
    daily_rate=models.FloatField()
    #each movie needs to be associated with a genre(if a genre is deleted all the movies associated are deleted)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

    #adding a new field date_created
    date_created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



