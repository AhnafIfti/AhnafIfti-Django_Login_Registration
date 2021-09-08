from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    website_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pic', blank=True)

    def __str__(self):
        return self.user.username