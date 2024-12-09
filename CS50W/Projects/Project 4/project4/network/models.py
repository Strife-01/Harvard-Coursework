from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class UserFollowingUser(models.Model):
    follower_id = models.IntegerField()
    following_id = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower_id', 'following_id'], name='name of constraint')
        ]

    def __str__(self):
        return f"{self.follower_id} is following {self.following_id}"


class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    text = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} by {self.poster} at {self.timestamp}"


class Comments(models.Model):
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comm = models.CharField(max_length=2000)
    comm_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comm} on {self.commented_post} by {self.comment_owner} at {self.comm_timestamp}"
