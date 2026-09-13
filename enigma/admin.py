from django.contrib import admin

from .models import Enigma

# Register your models here.
@admin.register(Enigma)
class EnigmaAdmin(admin.ModelAdmin):
    list_display = ("senha",)