from django.contrib import admin

from .models import Address, Author, Book, Country


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        "author",
        "rating",
    )
    list_display = ("title", "author")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    list_display_links = (
        "first_name",
        "last_name",
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "post_code")


admin.site.register(Country)
