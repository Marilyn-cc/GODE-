from django.db import models
from django.core.validators import MinValueValidator

class Cow(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('dry', 'Dry'),
        ('sold', 'Sold'),
    ]

    tag = models.CharField(max_length=32, unique=True)  # ear tag / identifier
    name = models.CharField(max_length=64, blank=True)
    breed = models.CharField(max_length=64, blank=True)
    dob = models.DateField(null=True, blank=True)
    parity = models.PositiveIntegerField(default=0)  # lactation number
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tag} - {self.name or 'Unnamed'}"


class MilkYield(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, related_name='yields')
    date = models.DateField()
    morning = models.DecimalField(max_digits=7, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    evening = models.DecimalField(max_digits=7, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    recorded_by = models.CharField(max_length=64, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cow', 'date')
        ordering = ['-date']

    @property
    def total(self):
        return (self.morning or 0) + (self.evening or 0)

    def __str__(self):
        return f"{self.cow.tag} - {self.date} : {self.total} L"


class ProductionSummary(models.Model):
    # optional daily aggregate if your dashboard shows totals per day
    date = models.DateField(unique=True)
    total_liters = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    note = models.CharField(max_length=128, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - {self.total_liters} L"
