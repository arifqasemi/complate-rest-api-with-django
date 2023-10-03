from django.contrib import admin
from .models import Movie,StreamPlateform,Review
# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamPlateform)
admin.site.register(Review)