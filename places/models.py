from django.db import models

class Place(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField('Описание', blank=True)
  lng = models.FloatField('Долгота')
  lat = models.FloatField('Широта')

  def __str__(self):
    return self.title

class Image(models.Model):
  place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
  image = models.ImageField('Картинка')
  order = models.PositiveIntegerField('Порядок', default=0)

  class Meta:
    ordering = ['order']

  def __str__(self):
    return f'{self.place.title} — {self.order}'
