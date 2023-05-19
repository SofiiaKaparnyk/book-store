from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Address(models.Model):
    street = models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.street}"

    class Meta:
        verbose_name_plural = "Address"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name.title()} ({self.last_name.title()})"


class Country(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        Author, null=True, on_delete=models.CASCADE, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country, related_name="books")
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.author})"
