import json
from django.shortcuts import render
from places.models import Place

import json
from django.shortcuts import render
from places.models import Place


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
                },
            }
            for place in places
        ],
    }
    return render(request, 'index.html', {'geojson': geojson})
