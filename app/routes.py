from django.shortcuts import render, redirect
from django.utils.timezone import now
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.urls import path

from app.models import (
    User,
    Note,
)

from events.models import Event

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from utils import uuid
from markdown import markdown


def note_all(request):
    Event.info(name='note_all', request=request)
    notes = [
        Note.objects.filter(pid=pid).first()
        for pid in request.session.get('notes', [])
    ]
    return render(request, "index.html", dict(notes=notes))


@csrf_exempt
def new_note(request):
    name = request.headers.get("hx-prompt", "")
    body = f'''
# {name}

This is your new note.

1. Click here to edit.
2. Anyone with a link to this file will be able to edit.
3. First line is the name of the note
'''
    note = Note(
        pid=uuid(),
        name=name,
        body=body.strip(),
    )
    note.save()
    Event.info(name='note_new', request=request, body=dict(pid=note.pid))

    return HttpResponse("", headers={"hx-redirect": f"/notes/{ note.pid }"})


def get_name(txt):
    return txt.strip().split("\n")[0].replace("#", "")


@csrf_exempt
def details(request, pid):
    Event.info(name='note_details', request=request, body=dict(pid=pid))
    note = Note.objects.filter(pid=pid).first()

    if not note:
        return HttpResponse("Note was not found")

    notes = request.session.get('notes', [])
    if note.pid in notes:
        notes.remove(note.pid)

    notes.insert(0, note.pid)

    request.session['notes'] = notes

    if request.method == "POST":
        note.body = request.POST.get('body', note.body)
        note.name = get_name(note.body)
        note.locked_to = None
        note.save()
        return HttpResponse("", headers={"hx-redirect": f"/notes/{ note.pid }"})

    return render(request, "details.html", dict(note=note, body=markdown(note.body)))
    # return HttpResponse("ok")


@csrf_exempt
def renew_lock(request, pid):
    note = Note.objects.filter(pid=pid).first()

    if not note:
        return HttpResponse("Note was not found")
    note.locked_to = now() + timedelta(seconds=15)
    note.save()
    return HttpResponse("Locked.. only you can edit this note.")


@csrf_exempt
def lock(request, pid):
    note = Note.objects.filter(pid=pid).first()

    if not note:
        return HttpResponse("Note was not found")

    if note.locked_to and note.locked_to >= now():
        return HttpResponse("Sorry, it's locked")

    note.locked_to = now() + timedelta(seconds=15)
    note.save()
    return render(request, "editor.html", dict(note=note))


def about(request):
    return render(request, "about.html")


urlpatterns = [
    path("", note_all),
    path("about", about),
    path("new_note", new_note),
    path("renew_lock/<str:pid>", renew_lock),
    path("lock/<str:pid>", lock),
    path("notes/<str:pid>/", details),
]
