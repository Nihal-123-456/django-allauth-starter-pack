from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileImageForm
from .models import Profile
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html', context)

@login_required
def edit_profile_image_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # request.POST receives any form data excluding files that was posted via the form while request.FILES receives any file(image, pdf e.t.c) that was posted
        form = ProfileImageForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile image updated successfully.")
            return redirect('account_profile')
        else:
            messages.error(request, "There was an error updating your profile image. Please check the form.")
    else:
        # when making changes to an existing object we need to pass that object as instance to the form
        form = ProfileImageForm(instance=profile)
    # rendering request.user.profile instead of the profile variable to show the profile.image directly from the db instead of the bound form
    return render(request, 'profile/edit_profile.html', {'form': form, 'profile': request.user.profile}) 