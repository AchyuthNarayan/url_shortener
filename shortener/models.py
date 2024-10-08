from django.db import models
from django.utils.crypto import get_random_string

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    shortened_url = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = get_random_string(6)  # Generate a random 6-character string
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.original_url} -> {self.shortened_url}"
