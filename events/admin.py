from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('created', 'level', 'name', 'email', 'country', 'ref', 'val1', 'val2', 'sid', 'url', 'ip', 'is_bot')
    list_filter = ('level', 'is_bot', 'is_mobile', 'is_tablet', 'is_pc')
    search_fields = ('name', 'email', 'country', 'ref', 'sid', 'ip')
    readonly_fields = ('created',)

    fieldsets = (
        (None, {
            'fields': ('created', 'level', 'name', 'email', 'country', 'ref', 'sid', 'url', 'val1', 'val2', 'val3', 'ip', 'body')
        }),
        ('Device Info', {
            'fields': ('user_agent', 'device', 'browser', 'browser_family', 'is_mobile', 'is_tablet', 'is_touch_capable', 'is_pc', 'is_bot')
        }),
        ('OS Info', {
            'fields': ('os', 'os_family', 'os_version')
        }),
        ('Device Details', {
            'fields': ('device_family', 'device_brand', 'device_model')
        }),
    )

    date_hierarchy = 'created'
    list_per_page = 50
