from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction_Categories, Auction_Listings, Comments, Bids, Watchlist


CATEGORIES = tuple([(index, cat) for index, cat in enumerate([cat.name for cat in Auction_Categories.objects.all()])])
CATEGORIES_ID = tuple([ cat for cat in [cat.id for cat in Auction_Categories.objects.all()]])

class CreateListingForm(forms.Form):
    title = forms.CharField(max_length=64, label="Auction Listing Title", required=True)
    description = forms.CharField(max_length=1000, label="Auction Listing Description", required=False)
    image_url = forms.URLField(label="Auction Listing Image URL", required=False)
    image_alt = forms.CharField(label="Auction Listing Image Alternative Text", required=True, initial="Image Alt Text")
    auction_categories_id = forms.ChoiceField(label="Category", required=False, choices=CATEGORIES)


class CreateBidForm(forms.Form):
    bid = forms.FloatField(label="Bid", required=True)


class CreateCommentsForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, label="Leave a comment")


def index(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "auctions/index.html", {
            "categories": None,
            "listings": Auction_Listings.objects.filter(is_auction_active=True),
        })


def listing(request, listing):
    if request.method == "POST":
        l = Auction_Listings.objects.get(pk=listing)

        if request.POST.get("deactivate"):
            l.is_auction_active = False
            l.save()
            return HttpResponseRedirect(reverse("index"))
        
        if request.POST.get("watchlist"):
            if watch := Watchlist.objects.filter(user_id=request.user.id, auction_listing_id=l.id):
                return HttpResponseRedirect(reverse("index"))
            else:
                watch = Watchlist(user_id=request.user.id, auction_listing_id=l.id)
                watch.save()
                return HttpResponseRedirect(reverse("index"))

        if request.POST.get("remove_watchlist"):
            Watchlist.objects.filter(user_id=request.user.id, auction_listing_id=l.id).delete()
            return HttpResponseRedirect(reverse("index"))
        
        if request.POST.get("place_bid"):

            form = CreateBidForm(request.POST)
            bid = float(form["bid"].value())

            if bid:
                bids = Bids.objects.filter(auction_listing_id=l.id)
                nr_bids = len(bids)
                highest_bid = 0
                if nr_bids > 0:
                    for b in bids:
                        if b.bid > highest_bid:
                            highest_bid = b.bid
                    if highest_bid > bid:
                        return HttpResponseRedirect(reverse("index"))
                bid = Bids(bid=bid, user_id=request.user.id, auction_listing_id=l.id)
                bid.save()
                return HttpResponseRedirect(reverse("index"))

        if request.POST.get("place_comment"):

            com_form = CreateCommentsForm(request.POST)
            comment = com_form["comment"].value()

            comm = Comments(content=comment, auction_listing_id=l.id, user_id=request.user.id)
            comm.save()
            return HttpResponseRedirect(reverse("index"))


    else:
        l = Auction_Listings.objects.get(pk=listing)
        creator = User.objects.get(pk=l.user_id.id)
        category = str(l.auction_categories_id).split()[1]

        is_watchlisted = False
        if watch := Watchlist.objects.filter(user_id=request.user.id, auction_listing_id=l.id):
            is_watchlisted = True
        
        bids = Bids.objects.filter(auction_listing_id=l.id)
        nr_bids = len(bids)
        highest_bid = 0
        highest_bidder = None
        if nr_bids > 0:
            for bid in bids:
                if bid.bid > highest_bid:
                    highest_bid = bid.bid
                    highest_bidder = User.objects.get(pk=bid.user_id)

        comments = []
        comms = Comments.objects.all()
        for com in comms:
            comments.append((com.content, User.objects.get(pk=com.user_id).username))

        return render(request, "auctions/listing.html", {
            "form": CreateBidForm(),
            "listing": l,
            "creator": creator,
            "category": category,
            "is_watchlisted": is_watchlisted,
            "nr_bids": nr_bids,
            "highest_bid": highest_bid,
            "highest_bidder": highest_bidder,
            "comments": comments,
            "com_form": CreateCommentsForm()
        })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST)
        if form.is_valid:
            title = form["title"].value()
            description = form["description"].value()
            image_url = form["image_url"].value()
            image_alt = form["image_alt"].value()
            auction_categories_id = form["auction_categories_id"].value()
            if auction_cat := Auction_Categories.objects.get(pk=int(auction_categories_id) + 1):
                listing = Auction_Listings(title=title, description=description, image_url=image_url, image_alt=image_alt, user_id=request.user, auction_categories_id=auction_cat)
            else:
                listing = Auction_Listings(title=title, description=description, image_url=image_url, image_alt=image_alt, user_id=request.user)

            listing.save()

            # Make server side validation 
            return HttpResponseRedirect(reverse("index"))
        else:
            form = CreateListingForm(form)
            return render(request, "auctions/create_listing.html", {
            "error": "Enter a valid form",
            "form": form
        })
    else:
        form = CreateListingForm()
        return render(request, "auctions/create_listing.html", {
            "form": form
        })


def watchlist(request):
    
    if request.method == "POST":
        pass
    else:
        listing_ids = [listing.auction_listing_id for listing in Watchlist.objects.filter(user_id=request.user.id)]
        listings = []
        for l_id in listing_ids:
            listings.append(Auction_Listings.objects.filter(id=l_id))
        print(listings)
        return render(request, "auctions/watchlist.html", {
            "listings_": listings
        })


def categories(request):
    cat_name = [cat for _, cat in CATEGORIES]
    cat_id = [cat_id for cat_id in CATEGORIES_ID]
    
    cat = []

    for i in range(len(cat_name)):
        cat.append((cat_id[i], cat_name[i]))

    return render(request, "auctions/categories.html", {
        "categories": cat
    })


def categories_listings(request, category):
    if request.method == "POST":
        pass
    else:
        return render(request, "auctions/categories_listings.html", {
            "listings": Auction_Listings.objects.filter(is_auction_active=True, auction_categories_id=category),
        })