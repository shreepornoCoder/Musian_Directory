from django.db import models
from author.models import Author
from datetime import datetime

# Create your models here.
class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=50, default=" ")
    musician = models.ForeignKey(to=Author, on_delete=models.CASCADE, default=" ")
    release_date = models.DateField(default=datetime.today())

    ratings = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    rating = models.TextField(choices=ratings)

    def __str__(self):
        return self.album_title
