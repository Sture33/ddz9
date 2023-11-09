from django.db import models


# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.pk}'
