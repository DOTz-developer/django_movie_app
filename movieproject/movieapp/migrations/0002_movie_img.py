# Generated by Django 4.1.7 on 2023-03-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="img",
            field=models.ImageField(default="abcd", upload_to="pics"),
            preserve_default=False,
        ),
    ]