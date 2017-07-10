from django.contrib import admin

from core.models import Business, BusinessSegment


class BusinessSegmentAdmin(admin.ModelAdmin):
    model = BusinessSegment


class BusinessAdmin(admin.ModelAdmin):
    model = Business


admin.site.register(BusinessSegment, BusinessSegmentAdmin)
admin.site.register(Business, BusinessAdmin)
