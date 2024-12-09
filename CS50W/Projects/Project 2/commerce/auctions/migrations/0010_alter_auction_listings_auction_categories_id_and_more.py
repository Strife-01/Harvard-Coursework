# Generated by Django 4.2.7 on 2023-12-04 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0009_alter_auction_listings_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auction_listings",
            name="auction_categories_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="category",
                to="auctions.auction_categories",
            ),
        ),
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
                (
                    "auction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="auction",
                        to="auctions.auction_listings",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_watchlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]