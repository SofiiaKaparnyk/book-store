# Generated by Django 4.2.1 on 2023-05-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0002_book_author_book_is_bestselling_alter_book_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]