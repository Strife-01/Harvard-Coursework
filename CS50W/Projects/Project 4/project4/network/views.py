from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

import json

from .models import User, Post, Comments, UserFollowingUser


def index(request):
    return render(request, "network/index.html")


def posts(request):
    if request.method == "GET":

        # Get the ith start post and ith end post
        start = int(request.GET["start"])
        end = int(request.GET["end"])
        
        # Turn start and end posts into indexes
        start -= 1

        # Query the database for the needed posts
        try:
            posts = Post.objects.order_by("-timestamp")[start:end]
        except IndexError:
            posts = None
        
        posts_list = []
        if posts is not None:
            # Get the elements needed in the database
            for post in posts:
                # TODO: Get the comments 
                # post_comments = Comments.objects.filter()

                # The edit allow function checking
                viewer_owner = True if request.user.username == post.poster.username else False

                p = {
                    "post_owner": post.poster.username,
                    "post_text": post.text,
                    "post_likes": post.like_count,
                    "post_timestamp": post.timestamp,
                    "post_id": post.id,
                    "viewer_owner": viewer_owner,
                    "comments": []
                }
                posts_list.append(p)

        return JsonResponse({
            "posts": posts_list
        }, status=201)
        
    else:
        return JsonResponse({
            "error": "GET request required."
        }, status=400)


@login_required
@csrf_exempt
def edit_post(request, post_id):
    if request.method == "PUT":
        text = json.loads(request.body)["text"]
        print(text)
        post = Post.objects.get(pk=post_id)
        post.text = text
        post.save()
        return JsonResponse({
            "success": ""
        }, status=201)
    else:
        return JsonResponse({
            "error": "PUT message required"
        }, status=400)


@login_required
def posts_by_user(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(poster=user).order_by("-timestamp")
    viewer_username = request.user.username
    posts_list = []
    for post in posts:
        post_text = post.text
        post_like_count = post.like_count
        post_timestamp = post.timestamp
        # Add Comments
        posts_list.append({
            "post_text": post_text,
            "post_like_count": post_like_count,
            "post_timestamp": post_timestamp,
            "post_id": post.id
        })

    return JsonResponse({
            "posts": posts_list,
            "viewer_username": viewer_username,
        }, status=201)


@login_required
def profile_page(request, username):
    if request.method == "GET":
        try:
            if viewing_user := User.objects.get(username=username):
                
                # Check if the user is following the viewing user
                if is_following := UserFollowingUser.objects.filter(follower_id=request.user.id, following_id=viewing_user.id):
                    follow = True 
                else:
                    follow = False

                # Get the number of followers and the number of following users
                followers = UserFollowingUser.objects.filter(following_id=viewing_user.id).count()
                following = UserFollowingUser.objects.filter(follower_id=viewing_user.id).count()

                return render(request, "network/profile_page.html", {
                    "username": username,
                    "button": follow,
                    "nr_followers": followers,
                    "nr_following": following
                })
        except:
            return HttpResponse(f"404 {username} not in database", content_type='text/plain')
    else:
        return JsonResponse({
            "error": "GET request required."
        }, status=400)


@login_required
def following_index(request):
    return render(request, "network/following.html")


@login_required
def following(request):
    if request.method == "GET":

        # Get the ith start post and ith end post
        start = int(request.GET["start"])
        end = int(request.GET["end"])
        
        # Turn start and end posts into indexes
        start -= 1

        # Query the database for the needed posts
        try:
            # Get the followed friends
            followed_users = []
            followed = UserFollowingUser.objects.filter(follower_id=request.user.id)
            for f in followed:
                followed_users.append(User.objects.get(pk=f.following_id))
            
            posts = Post.objects.order_by("-timestamp").filter(poster__in=followed_users)[start:end]
        except IndexError:
            posts = None
        print(posts)
        
        posts_list = []
        if posts is not None:
            ...
            # Get the elements needed in the database
            for post in posts:
                # TODO: Get the comments 
                # post_comments = Comments.objects.filter()

                # The edit allow function checking

                p = {
                    "post_owner": post.poster.username,
                    "post_text": post.text,
                    "post_likes": post.like_count,
                    "post_timestamp": post.timestamp,
                    "post_id": post.id,
                    "comments": []
                }
                posts_list.append(p)

        return JsonResponse({
            "posts": posts_list
        }, status=201)
        
    else:
        return JsonResponse({
            "error": "GET request required."
        }, status=400)


@csrf_exempt
def follow_user(request, username):
    if request.method == "PUT":
        action = json.loads(request.body)["action"]
        user_id = request.user.id
        following_id = User.objects.get(username=username).id
        if action == "follow":
            follow = UserFollowingUser(follower_id=user_id, following_id=following_id)
            follow.save()
        elif action == "unfollow":
            follow = UserFollowingUser.objects.get(follower_id=user_id, following_id=following_id)
            follow.delete()
    
    return JsonResponse({
        "success": ""
    }, status=201)


@login_required
def add_new_post(request):
    if request.method == "POST":
        
        # Retrieve post content
        text = request.POST["text"]
        
        # Validate content
        if len(text) < 1 or len(text) > 2000:
            return render(request, "network/add_new_post.html", {
                "error": "Post must be between 1 and 2000 characters..."
            })

        # Create post
        new_post = Post(poster=request.user, text=text)
        new_post.save()
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, "network/add_new_post.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
