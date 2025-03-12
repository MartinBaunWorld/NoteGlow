from django.core.management.base import BaseCommand, CommandError
from events.models import Event
from django.utils import timezone

from datetime import timedelta


class Command(BaseCommand):
    help = "Clears events so they don't fill up too much"

    def handle(self, *args, **options):
        last_14_days = timezone.now() - timedelta(days=14)
        Event.objects.filter(created__lt=last_14_days).delete()

        self.stdout.write(
            self.style.SUCCESS('Successfully cleaned events')
        )

