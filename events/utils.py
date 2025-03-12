from json import dumps

from .models import Event


def _event(request, level, name, body, email=None):

    # TODO work with authorization as well
    if email is None and request.user.is_authenticated:
        email = request.user.email
    else:
        email = "unknown"

    # ip = get_ip()

    model = Event(
        level=level.lower(),
        name=name.lower(),
        ip='',
        country='',
        # ip=ip,
        # country=ip2name(ip),
        email=str(email).lower(),
        body=dumps(body),
    )
    model.save()
    return model


def info(request, name, body, email=None):
    return _event(request, "info", level, body, email)


def warn(request, name, body, email=None):
    return _event(request, "warn", level, body, email)


def err(request, name, body, email=None):
    return _event(request, "err", level, body, email)
