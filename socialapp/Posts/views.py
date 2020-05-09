from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post, Comment, Reply, Like
from Accounts.models import UserInfo

# Create your views here.
def post(request):
  if request.method == "POST":
    #author, pub_date, content
    username = request.POST['username']
    user = User.objects.get(username=username)
    author = UserInfo.objects.get(user=user)
    content = request.POST['content']
    pub_date = timezone.now()
    
    post = Post.objects.create(author=author, content=content, pub_date=pub_date)
    post.save()
    return HttpResponseRedirect(reverse('index'))
  return HttpResponseRedirect(reverse('index'))
  
def post_like(request):
  if request.method == 'POST':
    post_id= request.POST['post']
    username = request.POST['username']
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(username=username)
    author = UserInfo.objects.get(user=user)

    try:
      like_available = post.likes.get(author=author)
      post.likes.remove(like_available)
      return JsonResponse({'likes': str(post.likes.count()), 'liked': False})
    except Like.DoesNotExist:
      like = Like.objects.get(author=author)
      post.likes.add(like)
    return JsonResponse({'likes':str(post.likes.count()),'liked': True})
  return HttpResponseRedirect(reverse('index'))
  
def comment_like(request):
  if request.method == 'POST':
    username = request.POST['username']
    comment_id= request.POST['comment']
    comment = Comment.objects.get(pk=comment_id)
    user = User.objects.get(username=username)
    author = UserInfo.objects.get(user=user)
    try:
      like_available = comment.likes.get(author=author)
      comment.likes.remove(like_available)
    except Like.DoesNotExist:
      like = Like.objects.get(author=author)
      comment.likes.add(like)
    return HttpResponseRedirect(reverse('index'))
  return HttpResponseRedirect(reverse('index'))
  
def reply_like(request):
  if request.method == 'POST':
    username = request.POST['username']
    reply_id= request.POST['reply']
    reply = Reply.objects.get(pk=reply_id)
    user = User.objects.get(username=username)
    author = UserInfo.objects.get(user=user)
    try:
      like_available = reply.likes.get(author=author)
      reply.likes.remove(like_available)
    except Like.DoesNotExist:
      like = Like.objects.get(author=author)
      reply.likes.add(like)
    return HttpResponseRedirect(reverse('index'))
  return HttpResponseRedirect(reverse('index'))
  
def comment(request):
  if request.method == "POST":
    #author, pub_date, content
    username = request.POST['username']
    post = request.POST['post']
    post = Post.objects.get(pk=post)
    user = User.objects.get(username=username)
    author = UserInfo.objects.get(user=user)
    comment = request.POST['comment']
    pub_date = timezone.now()
    
    comment = Comment.objects.create(author=author, comment=comment,post=post, pub_date=pub_date)
    comment.save()
    return JsonResponse({'comment': str(comment.comment),})
  return HttpResponseRedirect(reverse('index'))
  
def reply(request):
  if request.method == "POST":
    #author, pub_date, content
    comment = request.POST['comment']
    comment = Comment.objects.get(pk=comment)
    username = request.POST['username']
    user = User.objects.get(username=username)
    author = UserInfo.objects.get(user=user)
    reply = request.POST['reply']
    pub_date = timezone.now()
    
    reply = Reply.objects.create(author=author, reply=reply, pub_date=pub_date, comment=comment)
    reply.save()
    return HttpResponseRedirect(reverse('index'))
  return HttpResponseRedirect(reverse('index'))
  
def post_view(request, post_id):
  post = Post.objects.get(pk=post_id)
  context = {
    'title':post.content,
    'posts': (post,),
    'user': post.author,
  }
  return render(request, 'Posts/post_view.html',context)
  
def edit_post(request, post_id):
  if request.method == 'POST':
    content = request.POST['content']
    post = Post.objects.get(pk=post_id)
    post.content = content
    post.save()
    return HttpResponseRedirect(reverse('post_view', args=(str(post.id),)))
  context = {
    'title': 'Edit Post',
    'post': Post.objects.get(pk=post_id),
    }
  return render(request, 'Accounts/editpost.html', context)
  
def people_liked(request, post_id):
 post = Post.objects.get(id=post_id)
 context = {
   'title': 'People who liked',
   'post': post,
   'likes': post.likes.all(),
 }
 return render(request,   'Posts/people_liked.html', context)
 
