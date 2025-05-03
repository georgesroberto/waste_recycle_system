"""Admin configuration for the GarbageReport and Contact models."""
from django.contrib import admin
from .models import GarbageReport, Contact

@admin.register(GarbageReport)
class GarbageReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'status')
    list_filter = ('status', 'wastetype', 'location')
    search_fields = ('name', 'email', 'location')
    list_editable = ('status',)
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'contactEmail')
    search_fields = ('fname', 'lname', 'contactEmail')