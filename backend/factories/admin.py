from django.contrib import admin

from .models import Brand, Color, Model


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "brand",
    ]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
