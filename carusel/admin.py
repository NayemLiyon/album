from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Carusel
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title']

admin.site.register(Carusel,AlbumAdmin)