from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import Form, UserRegister, SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
# Create your views here.



def tweet_list(request):
    tweet = Tweet.objects.all().order_by('-created_at')
    return render(request, 'app/tweet_list.html', {'tweet': tweet})

def About(request):
    return render(request, 'app/About.html')

def contactus(request):
   return render(request, 'app/contactus.html')
   
@login_required                
def create(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Form()
    return render(request, 'app/tweet_form.html', {'form': form})

@login_required
def edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Form(instance=tweet)
    return render(request, 'app/tweet_form.html', {'form': form})

@login_required    
def delete(request, tweet_id):
     tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
     
     if request.method == 'POST':
         tweet.delete()
         return redirect('tweet_list')
     return render(request, 'app/tweet_delete.html', {'tweet': tweet})
    
    
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) 
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegister()
    return render(request, 'registration/register.html', {'form': form})
    
  
def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('q')
        tweet = Tweet.objects.all().filter(user_id=search)
        return render(request, 'app/search_results.html', {'tweet':tweet})
    
    
    
    