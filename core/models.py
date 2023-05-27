from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


# Create your models here.
class profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(max_length=255, blank=True)
    profileimg = models.ImageField(
        upload_to="profile_images", default="blank_profile_pic.png"
    )
    location = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_image")
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user
