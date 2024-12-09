# Generated by Django 4.2.7 on 2023-12-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0011_auction_listings_watchlist_delete_watchlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Watchlist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.BigIntegerField()),
                ("auction_listing_id", models.BigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name="auction_listings",
            name="watchlist",
        ),
    ]
