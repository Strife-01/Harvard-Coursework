# Generated by Django 4.2.7 on 2023-12-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0002_auction_categories_auction_listings_comments_bids"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction_listings",
            name="image_alt",
            field=models.CharField(default="Image Alt Text", max_length=64),
        ),
    ]