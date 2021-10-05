from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    disc = models.TextField()
    image = models.ImageField(upload_to = 'albumphotos/')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title