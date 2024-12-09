# Generated by Django 4.2.7 on 2023-12-04 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0008_alter_auction_listings_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auction_listings",
            name="user_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
