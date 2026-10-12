from django.db import models


class Feedback(models.Model):
    WATER = 'Water'
    FIRE = 'Fire'
    STORM = 'Storm'
    STRUCTURAL = 'Structural'
    MOLD = 'Mold'
    OTHER = 'Other'

    DAMAGE_TYPE_CHOICES = [
        (WATER, 'Water Damage'),
        (FIRE, 'Fire Damage'),
        (STORM, 'Storm Damage'),
        (STRUCTURAL, 'Structural Damage'),
        (MOLD, 'Mold Damage'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=100)
    property_address = models.CharField(max_length=250)
    damage_type = models.CharField(max_length=20, choices=DAMAGE_TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property_address