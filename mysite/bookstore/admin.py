from django.contrib import admin

# Register your models here.
from .models import Book

#admin.site.register(Book)

class BookManager(admin.ModelAdmin):
    list_display = ['id','title','pub','price','market_price']
    list_display_links = ['title']

admin.site.register(Book,BookManager)