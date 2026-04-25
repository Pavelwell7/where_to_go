from django.db import models

class Place(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField('Описание', blank=True)
  lng = models.FloatField('Долгота')
  lat = models.FloatField('Широта')

  def __str__(self):
    return self.title

