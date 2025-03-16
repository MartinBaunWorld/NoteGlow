from django.contrib.auth.models import AbstractUser, User
from django.db.models import *


def uuid():
    # For some reasons Django don't like it in other way
    # We gotta please her
    from utils import uuid
    return uuid()




class CustomUser(AbstractUser):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created']


User = CustomUser



class Note(Model):
    created = DateTimeField(auto_now_add=True)
    pid = CharField(null=False, default=uuid, max_length=255, unique=True)
    name = CharField(null=False, default='', max_length=255, blank=True)
    body = TextField(null=False, default='', blank=True)
    locked_to = DateTimeField(null=True, default=None, blank=True)
    locked_by = CharField(null=False, default='', blank=True, max_length=255)


class NoteVersion(Model):
    created = DateTimeField(auto_now_add=True)
    note = ForeignKey(Note, on_delete=CASCADE)
    body = TextField(null=False, default='', blank=True)
