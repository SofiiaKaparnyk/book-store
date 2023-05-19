# Generated by Django 4.2.1 on 2023-05-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0007_rename_street_author_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("code", models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Address"},
        ),
        migrations.AddField(
            model_name="book",
            name="published_countries",
            field=models.ManyToManyField(
                related_name="books", to="book_outlet.country"
            ),
        ),
    ]