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


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'pid')
    search_fields = ('name', 'body', 'pid')
    readonly_fields = ('pid',)


@admin.register(NoteVersion)
class NoteVersionAdmin(admin.ModelAdmin):
    list_display = ('note', 'body')
    search_fields = ('note', 'body')
