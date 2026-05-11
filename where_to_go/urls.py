from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places import views as places_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', places_views.show_map),
    path('places/<int:place_id>/', places_views.place_details, name='place_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
