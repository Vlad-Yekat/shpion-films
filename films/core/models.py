from django.db import models
from datetime import date
from django.urls import reverse

from users.models import CustomUser


class Rubric(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/", null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="film_actor")
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130, unique=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ScreenShot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='media')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(CustomUser,
                               on_delete=models.deletion.CASCADE,
                               null=True,
                               blank=True)
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
