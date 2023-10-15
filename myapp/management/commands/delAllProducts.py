# Удаляем ВСЕ ТОВАРЫ!

from django.core.management.base import BaseCommand
from myapp.models import Product  # Замените на вашу модель Product

class Command(BaseCommand):
    help = 'Удаление всех товаров из базы данных'

    def handle(self, *args, **kwargs):
        # Удаляем все товары
        Product.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Все товары успешно удалены из базы данных.'))
