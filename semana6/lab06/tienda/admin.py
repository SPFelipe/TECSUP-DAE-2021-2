from django.contrib import admin

# Register your models here.
from .models import Categoria, Product

admin.site.register(Categoria)
admin.site.register(Product)