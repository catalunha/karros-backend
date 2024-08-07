from django.contrib import admin
from django.utils.html import format_html

from .models import Vehicle


def make_is_sold(modeladmin, request, queryset):
    queryset.update(is_sold=True)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    make_is_sold.short_description = "Mark isSold item"
    actions = [make_is_sold]
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
    def image_view(self, obj):
        if not obj.image:
            return format_html("")
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(
                obj.image.url
            )
        )

    image_view.short_description = "View image"

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
                "value",
                "year",
                "is_sold",
                "image_view",
            ]
        else:
            self.list_display = [
                "model",
                "color",
                "value",
                "year",
                "is_sold",
                "image_view",
            ]

        return super(VehicleAdmin, self).changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
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
