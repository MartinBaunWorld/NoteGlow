from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from events.models import Event
from hyperp.utils import timestamp
from orjson import loads
from pydantic import BaseModel
from utils import expect_form


def paginate(qs, page_size: int, page: int):
    paginator = Paginator(qs, page_size)
    total_objects = paginator.count
    total_pages = paginator.num_pages

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = []

    return objects, total_objects, total_pages


def event_dict(event):
    return dict(
        id=event.id,
        created=timestamp(event.created),
        level=event.level,
        name=event.name,
        email=event.email,
        country=event.country,
        ip=event.ip,
        body=loads(event.body),
        ref=event.ref,
    )


class EventLogForm(BaseModel):
    page_size: int = 10
    page: int = 1
    event_name: str = None


@csrf_exempt
@expect_form(EventLogForm)
def event_log(request, form):
    # TODO: ensure to limit for authorized user OR admin
    qs = Event.objects.all()

    if form.event_name:
        qs = qs.filter(name__icontains=form.event_name)

    events, total_objects, total_pages = paginate(
        qs,
        page_size=form.page_size,
        page=form.page,
    )

    return dict(
        msg="ok",
        data=[event_dict(event) for event in events],
        page=form.page,
        page_size=form.page_size,
        total_pages=total_pages,
        total_objects=total_objects,
    )
