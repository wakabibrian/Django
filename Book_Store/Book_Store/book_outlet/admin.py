from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # read only
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating", )  # field names as defined in the model
    list_display = ("title", "author", )  # adding columns


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
