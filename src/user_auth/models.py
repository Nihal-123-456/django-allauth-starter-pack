from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from helpers import cloudinary_init

# initializing cloudinary
cloudinary_init()

User = get_user_model()

def get_display_name(instance, *args, **kwargs):
    if instance.user.username:
        return f'profile-image-{instance.user.username}'
    return 'profile-image'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # cloudinary field

    # here we pass the get_display_name function as a callable so that the cloudinary field can call this function whenever it needs the public_id_prefix instead of calling the function immediately after the model is defined which may not provide the desired results

    # here the transformation option makes sure the image is compressed while maintaining quality during upload(quality: auto:good) and is converted to the best format (fetch_format: auto)
    
    image = CloudinaryField('image', null=True, blank=True, display_name=get_display_name, 
    tags=["user", "profile", "image"], 
    public_id_prefix="user_avatar",
    transformation=[{'quality': 'auto:good', 'fetch_format': 'auto'}],
    folder='profile_images') 

    def __str__(self):
        return self.user.username