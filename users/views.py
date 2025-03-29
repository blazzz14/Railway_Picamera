from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import HttpResponse

@login_required
def profile(request):
    # Get or create the user's profile
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Render the profile page
    response = render(request, 'registration/profile.html', {'profile': profile})
    
    # Prevent caching
    response['Cache-Control'] = 'no-store'  # Ensures that the page is not cached
    response['Pragma'] = 'no-cache'         # Older HTTP 1.0 standard
    response['Expires'] = '0'               # Sets the expiration to 0
    
    return response
