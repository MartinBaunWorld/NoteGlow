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
    NoteVersion,
)

from events.models import Event

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup

from utils import uuid
from state import clean_html



body = """
<h1>Test</h1><p>This is your new note.</p><p><br></p><p>1. Click here to edit.</p><p>2. Anyone with a link to this file will be able to edit.</p><p>3. First line in the note is the title</p><p>4. When you open a note it will be added to "My Notes"</p>""".strip()

body = ""


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
    body = f'<h1>{name}</h1><p>This is your new note.</p><p><br></p><p>1. Click here to edit.</p><p>2. Anyone with a link to this file will be able to edit.</p><p>3. First line in the note is the title</p><p>4. When you open a note it will be added to "My Notes"</p>'
    note = Note(
        pid=uuid(),
        name=name,
        body=body.strip(),
    )
    note.save()
    Event.info(name='note_new', request=request, ref=note.pid)

    return HttpResponse("", headers={"hx-redirect": f"/notes/{ note.pid }"})


def get_name(txt):
    return txt.strip().split("\n")[0].replace("#", "")

def get_name(body):
    soup = BeautifulSoup(body, 'html.parser')
    first_element = soup.find()  # Retrieves the first tag in the document
    if first_element:
        return first_element.get_text(strip=True)
    else:
        return 'Unknown Name'



def add_note_to_session(request, note):
    # TODO could probably be done more efficient
    # but django likes to play games
    notes = request.session.get('notes', [])
    if note.pid in notes:
        notes.remove(note.pid)

    notes.insert(0, note.pid)

    request.session['notes'] = notes


@csrf_exempt
def details(request, pid):
    note = Note.objects.filter(pid=pid).first()

    if not note:
        Event.info(name='note_details', request=request, ref=pid, val1=404)
        # TODO nicer message
        return HttpResponse("Note was not found")

    Event.info(name='note_details', request=request, ref=pid, val1=200)
    
    add_note_to_session(request, note)

    return render(request, "details.html", dict(note=note))


@csrf_exempt
def note_edit(request, pid):
    note = Note.objects.filter(pid=pid).first()

    if not note:
        Event.info(name='note_edit', request=request, ref=pid, val1=404)
        # TODO nicer message
        return HttpResponse("Note was not found")

    # TODO check log is the correct tab and if not say it is locked
    # if note.locked_to and note.locked_to >= now():
    #    return HttpResponse("Sorry, it's locked")

    version = NoteVersion(
        body=note.body,
        note=note,
    )
    version.save()

    Event.info(name='note_edit', request=request, ref=pid, val1=200, val2=str(version.id))

    note.body = clean_html(request.POST.get('body', note.body))
    note.name = get_name(note.body)
    note.save()
    return HttpResponse("", headers={"hx-redirect": f"/notes/{ note.pid }"})


@csrf_exempt
def renew_lock(request, pid):
    Event.info(name='renew_lock', request=request, ref=pid)
    note = Note.objects.filter(pid=pid).first()

    if not note:
        return JsonResponse({"msg": "Note was not found"}, status=404)
    note.locked_to = now() + timedelta(seconds=10)
    note.save()
    return JsonResponse({"msg": "ok"})


@csrf_exempt
def lock(request, pid):
    if request.method != 'POST':
        return redirect(f"/notes/{pid}")

    Event.info(name='lock', request=request, ref=pid)
    note = Note.objects.filter(pid=pid).first()

    if not note:
        return HttpResponse("Note was not found")

    if note.locked_to and note.locked_to >= now():
        return HttpResponse("Sorry, it's locked")

    note.locked_to = now() + timedelta(seconds=15)
    note.save()
    return render(request, "editor.html", dict(note=note))


def about(request):
    Event.info(name='about', request=request)
    return render(request, "about.html")


urlpatterns = [
    path("", note_all),
    path("about", about),
    path("new_note", new_note),
    path("renew_lock/<str:pid>", renew_lock),
    path("lock/<str:pid>", lock),
    path("notes/<str:pid>/", details),
    path("note_edit/<str:pid>/", note_edit),
]
