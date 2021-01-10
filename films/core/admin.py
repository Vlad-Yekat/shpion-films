from django.contrib import admin

from .models import Movie, Rubric, Actor, ScreenShot, Review


admin.site.register(Rubric)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(ScreenShot)
admin.site.register(Review)
