import uuid

from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


def cv_upload_path(instance, filename):
    # Random file name, so nobody can guess another visitor's CV path.
    return f"cvs/{uuid.uuid4().hex}.pdf"


class Profile(models.Model):
    """Professional profile. Field names match the iOS model `ProfessionalProfile`."""

    # Values used by the iOS enum `LookingFor` (explore = «اكتشف» / just visiting)
    LOOKING_FOR_CHOICES = ["explore", "job", "internship", "collaboration"]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    job_title = models.CharField(max_length=150, blank=True)       # iOS: jobTitle (headline)
    bio = models.TextField(blank=True)
    education = models.CharField(max_length=255, blank=True)       # iOS: one field «التخصص · الجهة»
    experiences = models.JSONField(default=list, blank=True)       # [{"id","title","subtitle"}]
    skills = models.JSONField(default=list, blank=True)            # ["Python", "SQL"]
    looking_for = models.JSONField(default=list, blank=True)       # ["internship", "job"]
    linked_in = models.CharField(max_length=255, blank=True)       # iOS: linkedIn
    website = models.CharField(max_length=255, blank=True)
    preferred_contact = models.CharField(max_length=255, blank=True)  # e.g. contact email
    contact_goal = models.CharField(max_length=255, blank=True)

    cv = models.FileField(
        upload_to=cv_upload_path,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
    cv_original_name = models.CharField(max_length=255, blank=True)
    cv_uploaded_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.email or self.user.username}"