# Generated by Django 5.0.2 on 2024-03-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ytmusicfiles",
            name="downloaded_music_files",
            field=models.BinaryField(),
        ),
    ]
