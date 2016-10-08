from django.contrib import admin

from core.models import BusinessSegment


class BusinessSegmentAdmin(admin.ModelAdmin):
    model = BusinessSegment


admin.site.register(BusinessSegment, BusinessSegmentAdmin)
