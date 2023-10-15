# Чтобы запустить эту команду и удалить клиента по его ID,
# выполните следующую команду:
#         python manage.py delClient 1


from django.core.management.base import BaseCommand
from myapp.models import Client  # Замените на вашу модель Client

class Command(BaseCommand):
    help = 'Удаление клиента по ID'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='ID клиента')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']

        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR('Клиент с указанным ID не найден.'))
            return

        # Удаляем клиента
        client.delete()

        self.stdout.write(self.style.SUCCESS(f'Клиент с ID {client_id} успешно удален.'))
