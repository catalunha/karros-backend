from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "model",
        "color",
        "image",
        "value",
        "year",
        "is_sold",
    ]
