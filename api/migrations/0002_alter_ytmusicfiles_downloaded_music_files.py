# Generated by Django 5.0.2 on 2024-08-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ytmusicfiles",
            name="downloaded_music_files",
            field=models.FileField(blank=True, null=True, upload_to="youtube_files/"),
        ),
    ]
