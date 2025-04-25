import os
from datetime import datetime
from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    now = datetime.now()
    path = f'photos/{now.year}/{now.month}/{now.day}/user_{instance.id}'
    os.makedirs(os.path.join(settings.MEDIA_ROOT, path), exist_ok=True)
    return os.path.join(path, filename)

class UserDetail(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.name
