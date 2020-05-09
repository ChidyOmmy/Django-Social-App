from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo
from Posts.models import Post, Like

# Create your views here.
def index(request):
  if request.user.is_authenticated:
    user = UserInfo.objects.get(user=request.user)
    context = {
    'author': UserInfo.objects.get(user=request.user),
    'posts': Post.objects.order_by('-pub_date').all(),
    }
    return render(request, 'Accounts/home.html', context)
  return render(request, 'Accounts/index.html')

def profile(request):
  try:
    current_user = request.user.username
  except KeyError:
    return render(request, 'Accounts/login.html', {'message': 'You must be logged in first'})
  if current_user is not None:
    user = User.objects.get(username=current_user)
    author = UserInfo.objects.get(user=user)
    context = {
      'user': author,
      'title': f'{user.username}\'s profile',
    	'posts': Post.objects.filter(author=author).order_by('-pub_date').all(),
    }
    
    return render(request, 'Accounts/profile.html', context)
  return render(request, 'Accounts/error.html', {'error': 'User Not Found'})
  
def profile_view(request, username):
  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    return render(request, 'Accounts/error.html', {'error': 'User Not Found'})
  author = UserInfo.objects.get(user=user)
  context = {
    'user': author,
    'title': f'{user.username}\'s profile',
  	'posts': Post.objects.filter(author=author).all(),
  }
  return render(request, 'Accounts/profile.html', context)
  
def username_present(request, username):
    if User.objects.filter(username=username).exists():
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    email = request.POST['email']
    sex = request.POST['sex']
    try:
      user = User.objects.create_user(username=username, password=password, email=email)
    except IntegrityError:
      return render(request, 'Accounts/register.html', {'error':f'{username} already exists' })
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    userinfo = UserInfo.objects.create(user=user,sex=sex)
    if sex == 'F':
      userinfo.dp = 'profile_female.jpg'
    else:
      userinfo.dp = 'profile_male.jpg'
    userinfo.save()
    like = Like.objects.create(author=userinfo)
    like.save()
    context = {
      'user': user,
    }
    return render(request, 'Accounts/registered.html', context)
  
  return render(request, 'Accounts/register.html')
 
def login_view(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      return render(request, 'Accounts/login.html', {'logged_in': True, 'message':f'You\'re still logged in as {request.user.username}'})
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('index'))
    return render(request, 'Accounts/login.html', {'message': 'Invalid credentials'})
  return render(request, 'Accounts/login.html')
  
def logout_view(request):
  logout(request)
  return render(request, 'Accounts/login.html', {'message': 'Logged out'})
  

    


