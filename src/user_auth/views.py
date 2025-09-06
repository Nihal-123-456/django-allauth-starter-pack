from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def profile_view(request):
    return render(request, 'account/profile.html')