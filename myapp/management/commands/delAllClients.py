# Удаляем Всех Клиентов!

from django.core.management.base import BaseCommand
from myapp.models import Client  # Замените на вашу модель Client

class Command(BaseCommand):
    help = 'Удаление всех клиентов из базы данных'

    def handle(self, *args, **kwargs):
        # Удаляем всех клиентов
        Client.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Все клиенты успешно удалены из базы данных.'))
