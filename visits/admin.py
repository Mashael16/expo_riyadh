from django.contrib import admin

from .models import ProfileShareConsent, Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("user", "pavilion", "scanned_at", "confirmed_at")
    list_filter = ("pavilion",)


@admin.register(ProfileShareConsent)
class ProfileShareConsentAdmin(admin.ModelAdmin):
    list_display = ("user", "pavilion", "is_active", "granted_at", "revoked_at")
    list_filter = ("pavilion", "is_active")