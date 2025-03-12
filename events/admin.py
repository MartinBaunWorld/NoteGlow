from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('created', 'level', 'name', 'email', 'country', 'ip', 'ref')
    list_filter = ('level', 'country', 'created')
    search_fields = ('name', 'email', 'country', 'ip', 'ref')
    readonly_fields = ('created',)
    date_hierarchy = 'created'
    ordering = ('-created',)
    fieldsets = (
        (None, {
            'fields': ('created', 'level', 'name', 'email', 'country', 'ip', 'body', 'ref')
        }),
    )

admin.site.register(Event, EventAdmin)
