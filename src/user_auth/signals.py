from django.dispatch import receiver
from allauth.account.signals import email_confirmed, user_signed_up
from django.db.models.signals import post_delete, pre_save
import cloudinary.uploader
from .models import Profile


# a profile is created after a user confirms their email via the link sent to their email
@receiver(email_confirmed)
def create_user_profile(sender, request, email_address, *args, **kwargs):
    user = email_address.user
    Profile.objects.get_or_create(user=user)

# a profile is created after a user signs up via a social account e.g. google
@receiver(user_signed_up)
def create_user_profile_social(sender, request, user, **kwargs):
    if kwargs.get("sociallogin"):  
        Profile.objects.get_or_create(user=user)

# the profile image is removed from cloudinary storage if the profile is deleted
@receiver(post_delete, sender=Profile)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        # deleting from cloudinary
        cloudinary.uploader.destroy(instance.image.public_id) 

# the old profile image is removed from cloudinary storage if the user changes their image
@receiver(pre_save, sender=Profile)
def auto_delete_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False  

    try:
        old_profile = Profile.objects.get(pk=instance.pk)
    except Profile.DoesNotExist:
        return False

    old_image = old_profile.image
    new_image = instance.image

    if old_image and old_image != new_image:
        cloudinary.uploader.destroy(old_image.public_id)