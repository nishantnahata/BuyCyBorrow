import os
from django.db import models


def get_image_path(instance, filename):
    return os.path.join('templates/../static/images', str(instance.id), filename)

class Cycle(models.Model):
    photo = models.ImageField(upload_to=get_image_path,blank=True,null=True)
    name = models.CharField(max_length=40)
    is_borrowed = models.BooleanField(default=False)
    tire_radius = models.FloatField(default=8)
    threshold = models.FloatField(default=10)
    description = models.CharField(max_length=400)
    cost = models.FloatField(null=True, blank=True)

    def set_borrowed(self):
        self.is_borrowed = True

    @property
    def get_image_path(self):
        return os.path.join('templates/../static/images', str(self.id), self.photo.name)