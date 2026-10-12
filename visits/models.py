from django.conf import settings
from django.db import models

from expo.models import Pavilion


class Visit(models.Model):
    """A pavilion in the visitor's «My Expo Journey». Never deleted by consent changes."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="visits")
    pavilion = models.ForeignKey(Pavilion, on_delete=models.CASCADE, related_name="visits")
    scanned_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)   # «أكد زيارتي»

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "pavilion"], name="one_visit_per_pavilion"),
        ]
        ordering = ["-scanned_at"]

    def __str__(self):
        return f"{self.user} → {self.pavilion.name}"


class ProfileShareConsent(models.Model):
    """
    The visitor's permission for ONE pavilion to see their professional profile.
    Separate from Visit: revoking sets is_active=False and the Visit stays.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="consents")
    pavilion = models.ForeignKey(Pavilion, on_delete=models.CASCADE, related_name="consents")
    is_active = models.BooleanField(default=True)
    granted_at = models.DateTimeField()
    revoked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "pavilion"], name="one_consent_per_pavilion"),
        ]

    def __str__(self):
        state = "active" if self.is_active else "revoked"
        return f"{self.user} → {self.pavilion.name} ({state})"