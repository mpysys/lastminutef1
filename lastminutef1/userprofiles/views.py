from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Create your views here.

def user_profile(request):
    """ Display the user's profile"""
    userprofile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': userprofile,
    }

    return render(request, template, context)