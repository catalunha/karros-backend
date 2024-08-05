from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_filter = [
        "is_sold",
    ]
    # list_display = [
    #     "id",
    #     "user",
    #     "model",
    #     "color",
    #     "image",
    #     "value",
    #     "year",
    #     "is_sold",
    # ]
    # exclude = ["user"]

    def add_view(self, request, extra_context=None):
        if not request.user.is_superuser:
            self.exclude = ["user"]
        else:
            self.exclude = []
        return super(VehicleAdmin, self).add_view(request, extra_context)

    def change_view(self, request, object_id, extra_context=None):
        if not request.user.is_superuser:
            self.exclude = ["user"]
        else:
            self.exclude = []
        return super(VehicleAdmin, self).change_view(request, object_id, extra_context)

    def changelist_view(self, request, extra_context=None):
        print("VehicleAdmin.changelist_view")
        print("user", request.user)
        if request.user.is_superuser:
            self.list_display = [
                "id",
                "user",
                "model",
                "color",
                "image",
                "value",
                "year",
                "is_sold",
            ]
        else:
            self.list_display = [
                "model",
                "color",
                "image",
                "value",
                "year",
                "is_sold",
            ]

        return super(VehicleAdmin, self).changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        print("VehicleAdmin.save_model")
        try:
            print("obj.user", obj.user)
        except ObjectDoesNotExist:
            print("obj.user not exist")
            obj.user = request.user

        # obj.save()
        super().save_model(request, obj, form, change)

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         return True  # So they can see the change list page
    #     if request.user.is_superuser or obj.user == request.user:
    #         return True
    #     else:
    #         return False

    # has_delete_permission = has_change_permission
