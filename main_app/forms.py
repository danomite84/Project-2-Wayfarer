from django import forms
from .models import Profile, Post, City

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'firstname', 'lastname', 'currentcity', 'picture' ]

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'city', 'content', ]

class CityCreationForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'picture', 'country']