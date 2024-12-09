from django.contrib import admin

from .models import User, Auction_Categories, Auction_Listings, Comments, Bids

# Register your models here.
admin.site.register(User)
admin.site.register(Auction_Categories)
admin.site.register(Auction_Listings)
admin.site.register(Comments)
admin.site.register(Bids)