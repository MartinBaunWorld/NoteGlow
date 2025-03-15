from django.db.models import *
from django.contrib.auth.models import User
from user_agents import parse

from utils import get_ip
from state import ip2country


class Event(Model):
    created = DateTimeField(auto_now_add=True)

    LEVEL_CHOICES = (
        (0, 'Debug'),
        (1, 'Info'),
        (2, 'Warning'),
        (3, 'Error')
    )
    level = IntegerField(null=False, default=1, choices=LEVEL_CHOICES)
    name = CharField(max_length=256, null=False)
    email = CharField(max_length=256, null=False, default="")
    country = CharField(max_length=256, null=False, default="")
    ref = CharField(max_length=256, null=False, default="")
    sid = CharField(max_length=256, null=False, default='')
    url = CharField(max_length=256, null=False, default='')
    val1 = CharField(max_length=256, null=False, default='')
    val2 = CharField(max_length=256, null=False, default='')
    val3 = CharField(max_length=256, null=False, default='')
    ip = CharField(max_length=256, null=False, default="")
    body = TextField(null=False, default="{}")
    user_agent = CharField(max_length=1024, null=False, default='')
    device = CharField(max_length=256, null=False, default='')
    browser = CharField(max_length=256, null=False, default='')
    browser_family = CharField(max_length=256, null=False, default='')
    is_mobile = BooleanField(null=False, default=False)
    is_tablet = BooleanField(null=False, default=False)
    is_touch_capable = BooleanField(null=False, default=False)
    is_pc = BooleanField(null=False, default=False)
    is_bot = BooleanField(null=False, default=False)
    os = CharField(max_length=256, null=False, default='')
    os_family = CharField(max_length=256, null=False, default='')
    os_version = CharField(max_length=256, null=False, default='')
    device_family = CharField(max_length=256, null=False, default='')
    device_brand = CharField(max_length=256, null=False, default='')
    device_model = CharField(max_length=256, null=False, default='')

    def __str__(self):
        return f'{self.level} - {self.name} - {self.email}'

    @classmethod
    def debug(cls, **kwargs):
        return cls._create_event(level=0, **kwargs)

    @classmethod
    def info(cls, **kwargs):
        return cls._create_event(level=1, **kwargs)

    @classmethod
    def warn(cls, **kwargs):
        return cls._create_event(level=2, **kwargs)

    @classmethod
    def err(cls, **kwargs):
        return cls._create_event(level=3, **kwargs)

    @classmethod
    def _create_event(cls, level, request=None, **kwargs):
        user = getattr(request, 'user', None)
        if user and isinstance(user, User):
            kwargs.setdefault('email', user.email)

        ip = ""
        country = ""
        if request:
            kwargs.setdefault('ip', get_ip(request))
            kwargs.setdefault('country', ip2country(kwargs['ip']))

            user_agent = request.headers.get("User-Agent", "")
            ua = parse(user_agent)
            kwargs.setdefault('user_agent', user_agent)
            kwargs.setdefault('device', ua.device.family)
            kwargs.setdefault('browser', ua.browser.family)
            kwargs.setdefault('browser_family', ua.browser.family)
            kwargs.setdefault('is_mobile', ua.is_mobile)
            kwargs.setdefault('is_tablet', ua.is_tablet)
            kwargs.setdefault('is_touch_capable', ua.is_touch_capable)
            kwargs.setdefault('is_pc', ua.is_pc)
            kwargs.setdefault('is_bot', ua.is_bot)
            kwargs.setdefault('os', ua.os.family)
            kwargs.setdefault('os_family', ua.os.family or '')
            kwargs.setdefault('os_version', ua.os.version_string or '')
            kwargs.setdefault('device_family', ua.device.family or '')
            kwargs.setdefault('device_brand', ua.device.brand or '')
            kwargs.setdefault('device_model', ua.device.model or '')

        return cls.objects.create(level=level, **kwargs)
