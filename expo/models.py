from django.conf import settings
from django.db import models


class Pavilion(models.Model):
    # The id the iOS app uses everywhere, e.g. "p1-ai-future" (JSON: place_id)
    slug = models.SlugField(max_length=60, unique=True)

    # The text inside the pavilion's QR code, also typed manually, e.g. "AI-01"
    code = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    experience_type = models.CharField(max_length=100, blank=True)

    # Name of an image that already exists inside the iOS app, e.g. "photo-ai-city"
    photo = models.CharField(max_length=100, blank=True)

    # Contact information shown in the visitor's Journey
    contact_email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    # Users allowed to open this pavilion's dashboard
    staff = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="staffed_pavilions",
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.code = self.code.strip().upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"