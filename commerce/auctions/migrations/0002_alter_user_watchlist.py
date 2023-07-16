# Generated by Django 4.2.3 on 2023-07-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True, related_name="watching", to="auctions.listing"
            ),
        ),
    ]
