from django.contrib import admin
from .models import Photo, Reservation

# Model registration
admin.site.register(Photo)
admin.site.register(Reservation)
