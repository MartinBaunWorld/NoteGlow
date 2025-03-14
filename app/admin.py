from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username',]



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'level', 'name', 'email', 'country', 'ip', 'created',
        'is_mobile', 'is_bot', 'os', 'device'
    )

    list_filter = (
        'level', 'country', 'is_mobile', 'is_bot', 'os', 'created'
    )

    search_fields = (
        'name', 'email', 'ip', 'country', 'user_agent', 'device', 'os'
    )

    list_editable = ('level', )

    readonly_fields = [
        field.name for field in Event._meta.fields if field.name != 'level'
    ]

    fieldsets = (
        ('Basic Information', {
            'fields': ('level', 'name', 'email', 'country', 'created')
        }),
        ('Request', {
            'fields': ('body', 'ip', 'ref', 'sid', 'url')
        }),
        ('Device Information', {
            'fields': (
                'user_agent', 'device', 'browser', 'browser_family',
                'is_mobile', 'is_tablet', 'is_touch_capable', 'is_pc', 'is_bot',
                'os', 'os_family', 'os_version',
                'device_family', 'device_brand', 'device_model'
            )
        }),
    )

    date_hierarchy = 'created'
    list_per_page = 50


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'pid')
    search_fields = ('name', 'body', 'pid')
    readonly_fields = ('pid',)
