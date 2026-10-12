from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "job_title", "education", "looking_for", "updated_at")
    search_fields = ("user__email", "user__first_name", "job_title", "education")
    readonly_fields = ("created_at", "updated_at", "cv_uploaded_at")