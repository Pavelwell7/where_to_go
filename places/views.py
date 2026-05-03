from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place


def place_details(request, place_id):
  place = get_object_or_404(Place, id=place_id)

  json = {
    'title': place.title,
    'imgs': [image.image.url for image in place.images.all()],
    'description_long': place.description_long,
    'description_short': place.description_short,
  }

  return JsonResponse(json, json_dumps_params={'indent': 2, 'ensure_ascii': False})
