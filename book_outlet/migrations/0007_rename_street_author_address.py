# Generated by Django 4.2.1 on 2023-05-19 14:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0006_address_author_street"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="street",
            new_name="address",
        ),
    ]