from django.core.management.base import BaseCommand
from myapp.models import Client  # Замените на вашу модель Client

class Command(BaseCommand):
    help = 'Вывод списка клиентов с их ID'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()

        if clients:
            self.stdout.write(self.style.SUCCESS('Список клиентов с их ID:'))
            for client in clients:
                self.stdout.write(f'ID: {client.id}, Имя: {client.name}, Электронная почта: {client.email}')
        else:
            self.stdout.write(self.style.SUCCESS('Список клиентов пуст.'))
