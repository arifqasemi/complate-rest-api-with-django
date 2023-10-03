from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class StreamPlateform(models.Model):
    name = models.CharField(max_length=225)
    about = models.CharField(max_length=300)
    website = models.URLField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    plateform = models.ForeignKey(StreamPlateform, on_delete=models.CASCADE, related_name='movie',null=True)
    title = models.CharField(max_length=100, unique=False)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=100)
    avrg_rating = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    user_review = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=225, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return str(self.rating)

