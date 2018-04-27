from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_user = models.ForeignKey(User, related_name="profile_user", on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)


class Reviews(models.Model):
    reviewed_user = models.ForeignKey(User, related_name="reviewed_user", on_delete=models.CASCADE)
    reviewing_user = models.ForeignKey(User, related_name="reviewing_user", on_delete=models.CASCADE)
    review = models.CharField(max_length=500, blank=False)