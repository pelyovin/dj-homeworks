from django.contrib import admin

# Register your models here.
from .models import Book, Order


admin.site.register(Book)
admin.site.register(Order)
