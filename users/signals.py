from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.dispatch import receiver




def profileCreated(sender, instance, created, **kargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
        )

def profileDelete(sender, instance, **kargs):
    user = instance.user
    user.delete()


post_save.connect(profileCreated, sender = User)
post_delete.connect(profileDelete, sender = Profile)  
