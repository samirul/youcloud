# Generated by Django 5.0.2 on 2024-03-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_ytmusicfiles_downloaded_music_files"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ytmusicfiles",
            name="downloaded_music_files",
            field=models.FileField(upload_to="youtube_files"),
        ),
    ]
