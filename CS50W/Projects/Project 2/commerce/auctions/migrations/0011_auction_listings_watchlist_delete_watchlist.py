# Generated by Django 4.2.7 on 2023-12-04 15:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0010_alter_auction_listings_auction_categories_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction_listings",
            name="watchlist",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name="Watchlist",
        ),
    ]
