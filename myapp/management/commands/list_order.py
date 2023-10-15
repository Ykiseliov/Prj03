from django.core.management.base import BaseCommand
from myapp.models import Order  # Замените на вашу модель Order

class Command(BaseCommand):
    help = 'Просмотр заказов и их заказчиков'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()

        if orders:
            self.stdout.write(self.style.SUCCESS('Список заказов и их заказчиков:'))
            for order in orders:
                self.stdout.write(f'Заказ ID: {order.id}, Заказчик: {order.client.name}')
        else:
            self.stdout.write(self.style.SUCCESS('Список заказов пуст.'))
