# Generated by Django 4.2.7 on 2023-12-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mail", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="is_trash",
            field=models.BooleanField(default=False),
        ),
    ]