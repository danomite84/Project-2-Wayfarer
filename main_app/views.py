from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProfileCreationForm, PostCreationForm, CityCreationForm
from .models import Profile, Post, City
from django.contrib.auth.decorators import login_required
from smart_selects.db_fields import ChainedForeignKey


CITIES = [ 'Irvine' , 'New York'] 
# Create your views here.

def home(request):
    return render(request, 'home.html')

## PROFILES VIEWS

def profiles_index(request):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(profile=profile)
    context = {'profile': profile, 'posts' : posts}
    return render(request, 'profiles/index.html', context)

def new_profile(request):
    if request.method == "POST":
        profile_form = ProfileCreationForm(request.POST)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()

            return redirect('detail', new_profile.id)
    else:
        profile_form = ProfileCreationForm()
        context = {'profile_form' : profile_form}
        return render(request, 'profiles/new.html', context)

def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {'profile' : profile}

    return render(request, 'profiles/detail.html', context )


def profiles_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    if request.method == "POST":
        profile_form = ProfileCreationForm(request.POST, instance=profile)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            return redirect('detail', updated_profile.id)
    else:
        profile_form  = ProfileCreationForm(instance=profile)
        context = {'profileform': profile_form, 'profile' : profile}
        return render(request, 'profiles/edit.html', context)

def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_profile')
        else:
            error_message = "Invalid sign up - try again"
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'registration/signup.html', context)

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



def add_post(request, profile_id):
    if request.method == "POST":
        form = PostCreationForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.profile_id = profile_id
            
            new_form.save()

        return redirect('detail', profile_id)
    else:
        form = PostCreationForm()
        return render(request, 'posts/new.html', {'form': form, 'profile_id' : profile_id, 'citylist' : CITIES})


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        postform = PostCreationForm(request.POST, instance=post)
        if postform.is_valid():
            updated_post = postform.save()
            return redirect('postdetail', updated_post.id)
    else:
        postform = PostCreationForm(instance=post)
        context = {'postform': postform, 'post' : post}
        return render(request, 'posts/edit.html', context )

def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()

    return redirect("profiles_index")

def city_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {"cities" : cities})

def add_city(request):
    if request.method == "POST":
        form = CityCreationForm(request.POST)

        if form.is_valid():
            new_city = form.save()
            new_city.save()
            return redirect('citydetail', new_city.id)
        
    else :
        form = CityCreationForm()
        return render(request, 'cities/new.html', {'form': form})

def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city)
    print(posts)
    context = {'city': city, 'posts' : posts}
    return render(request, 'cities/detail.html', context)
