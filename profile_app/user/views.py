from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.
class UserForm(forms.ModelForm):
    """Form to update the user profile."""
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class UserProfileForm(forms.ModelForm):
    """Form to update the user profile."""
    class Meta:
        model = UserProfile
        fields = ("home_address", "phone_number", "location_x", "location_y")


@login_required
@transaction.atomic
def update_profile(request):
    """View to update the user profile."""
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("user:profile")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, "profile.html", {"user_form": user_form, "profile_form": profile_form})