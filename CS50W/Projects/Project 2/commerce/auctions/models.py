from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction_Categories(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id}) {self.name}"


class Auction_Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image_alt = models.CharField(max_length=64, default="Image Alt Text")
    auction_categories_id = models.ForeignKey(Auction_Categories, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="category")
    is_auction_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="user")

    def __str__(self):
        return f"{self.is_auction_active}: {self.title} from {self.auction_categories_id} with desc {self.description} and image {self.image_url}"


class Watchlist(models.Model):
    user_id = models.BigIntegerField()
    auction_listing_id = models.BigIntegerField()


class Comments(models.Model):
    content = models.CharField(max_length=500)
    user_id = models.BigIntegerField()
    auction_listing_id = models.BigIntegerField()

    def __str__(self):
        return f"{self.user_id} commented {self.comment} on {self.auction_listing_id}"


class Bids(models.Model):
    bid = models.FloatField()
    user_id = models.BigIntegerField()
    auction_listing_id = models.BigIntegerField()

    def __str__(self):
        return f"{self.user_id} bid {self.bid} on {self.auction_listing_id}"