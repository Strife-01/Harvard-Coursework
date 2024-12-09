# Generated by Django 4.2.7 on 2023-12-16 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("like_count", models.IntegerField(default=0)),
                ("text", models.CharField(max_length=2000)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "poster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("comm", models.CharField(max_length=2000)),
                ("comm_timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "comment_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "commented_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="network.post"
                    ),
                ),
            ],
        ),
    ]
