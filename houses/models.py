from django.db import models

# Create your models here.
class House(models.Model):

    """Model definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="Price")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="애완동물을 허용하시나요?")

    def __str__(self):
        return self.name