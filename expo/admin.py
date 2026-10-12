from django.contrib import admin

from .models import Pavilion


@admin.register(Pavilion)
class PavilionAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "slug", "organization", "contact_email")
    search_fields = ("name", "code", "slug", "organization")
    filter_horizontal = ("staff",)