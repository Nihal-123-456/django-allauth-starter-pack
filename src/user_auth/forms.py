from django import forms
from .models import Profile
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm, AddEmailForm, SetPasswordForm, ChangePasswordForm
from allauth.socialaccount.forms import DisconnectForm
from cloudinary.forms import CloudinaryFileField
import cloudinary.uploader
import logging

logger = logging.getLogger(__name__)

# updating all the default django allauth forms to add styling

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Email or Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Password'
        })
        self.fields['remember'].widget.attrs.update({
            'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'
        })

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Email'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Confirm Password'
        })

class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Email'
        })

class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'New Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Confirm New Password'
        })

class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Current Password'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'New Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Confirm New Password'
        })

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password1'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'New Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Confirm New Password'
        })

class CustomAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'New Email Address'
        })

class CustomDisconnectForm(DisconnectForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account'].widget.attrs.update({
            'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'
        })

class ProfileImageForm(forms.ModelForm):

    class Meta:
        model= Profile
        fields=['image']
        # here we are modifying the field widget to add styling and remove the default django "currently/clear" text while also keeping the upload options(display_name, tags e.t.c) of the cloudinary field
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                'id': 'user_avatar',
                'type': 'file',
                'aria-describedby': 'user_avatar_help',
                'accept': 'image/*'
            })
        }

    def clean(self):
        # self.data is a querydict that contains form data from all the inputs and fields inside the <form> element of the html file. Similarly self.files contain all the files. Whereas cleaned_data is a dictionary that contains only the validated data from the declared form fields.
        cleaned_data = super().clean()
        new_image = self.files.get("image")
        remove = self.data.get("image-clear")

        if not new_image and not remove:
            raise forms.ValidationError("Please provide an image or input.")
        if new_image and remove:
            raise forms.ValidationError("You cannot upload a new image and remove the current one at the same time.")

        return cleaned_data

    def save(self, commit=True):
        profile = super().save(commit=False)

        if commit and self.data.get('image-clear'):
            # removing imgae from cloudinary storage if the user chooses to remove their current image  
            if profile.image:
                try:
                    cloudinary.uploader.destroy(profile.image.public_id)
                except Exception as e:
                    logger.error(f"Cloudinary delete failed: {e}")
            profile.image = None

        if commit:
            profile.save()
        return profile