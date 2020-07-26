from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL as k


class Command(BaseCommand):
    help = 'Refreshes all KirlURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return k.objects.refresh_shortcodes(items = options['items'])
        