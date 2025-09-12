from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from helpers import cloudinary_init

# initializing cloudinary
cloudinary_init()

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True) # cloudinary field

    def __str__(self):
        return self.user.username