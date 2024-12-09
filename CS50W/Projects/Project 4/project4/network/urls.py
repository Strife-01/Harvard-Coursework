
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("edit/<int:post_id>", views.edit_post, name="edit_post"),
    path("posts/<str:username>", views.posts_by_user, name="posts_by_user"),
    path("add_new_post", views.add_new_post, name="add_new_post"),
    path("profile/<str:username>", views.profile_page, name="profile_page"),
    path("follow", views.following_index, name="following_index"),
    path("follow_user/<str:username>", views.follow_user, name="follow_user"),
    path("following", views.following, name="following"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
