# Generated by Django 4.2.3 on 2023-07-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0005_remove_post_comments_post_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
