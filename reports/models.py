# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class GarbageReport(models.Model):
    WASTE_TYPE_CHOICES = [
        ('organic', 'Organic'),
        ('inorganic', 'Inorganic'),
        ('mixed', 'Mixed'),
        ('household', 'Household'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending Collection'),
        ('Completed', 'Collected'),
    ]
    
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='garbage_reports', null=True)

    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    wastetype = models.CharField(max_length=100)  # Will store comma-separated values
    location = models.CharField(max_length=255)
    locationdescription = models.TextField()
    file = models.ImageField(upload_to='garbage_images/')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    
    def save(self, *args, **kwargs):
        if not self.date:
            now = timezone.now()
            self.date = now.strftime("%-I:%M%p ,\\r\\n %A %d %B %Y")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}'s report at {self.location}"

class Contact(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    contactEmail = models.EmailField(max_length=50)
    contactPhone = models.CharField(max_length=10)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.fname} {self.lname}'s message"