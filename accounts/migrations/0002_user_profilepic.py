# Generated by Django 5.0.2 on 2024-07-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profilePic",
            field=models.ImageField(default="default.png", upload_to="profile-pic"),
        ),
    ]
