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
    exclude = ["user"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         return True  # So they can see the change list page
    #     if request.user.is_superuser or obj.user == request.user:
    #         return True
    #     else:
    #         return False

    # has_delete_permission = has_change_permission
