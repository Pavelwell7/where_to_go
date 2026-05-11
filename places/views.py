from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place



def place_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=place_id
    )

    json = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'long_description': place.long_description,
        'short_description': place.short_description,
    }

    return JsonResponse(json, json_dumps_params={'indent': 2, 'ensure_ascii': False})

def show_map(request):
    places = Place.objects.all()
    geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat],
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('place_details', args=[place.id]),

                },
            }
            for place in places
        ],
    }
    return render(request, 'index.html', {'geojson': geojson})
