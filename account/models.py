from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profile_image', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Reviews(models.Model):
    reviewed_user = models.ForeignKey(User, related_name="reviewed_user", on_delete=models.CASCADE)
    reviewing_user = models.ForeignKey(User, related_name="reviewing_user", on_delete=models.CASCADE)
    review = models.CharField(max_length=500, blank=False)