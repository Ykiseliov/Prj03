# Добавляем пользователя

from django.core.management import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Добавление нового клиента'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Имя клиента')
        parser.add_argument('email', type=str, help='Электронная почта клиента')
        parser.add_argument('phone_number', type=str, help='Номер телефона клиента')
        parser.add_argument('address', type=str, help='Адрес клиента')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        phone_number = kwargs['phone_number']
        address = kwargs['address']

        # Создание нового клиента и сохранение его в базе данных
        client = Client.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address
        )

        self.stdout.write(self.style.SUCCESS(f'Клиент {client.name} успешно добавлен с ID {client.pk}'))
