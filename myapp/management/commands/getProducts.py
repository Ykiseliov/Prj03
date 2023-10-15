# Команда для вывода списка товаров, количество каждого и их id

from django.core.management.base import BaseCommand
from myapp.models import Product  # Замените на вашу модель Product

class Command(BaseCommand):
    help = 'Вывод списка товаров с количеством и ID'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        if products:
            self.stdout.write(self.style.SUCCESS('Список товаров с количеством и ID:'))
            for product in products:
                self.stdout.write(f'ID: {product.id}, Название: {product.name}, Количество: {product.quantity}')
        else:
            self.stdout.write(self.style.SUCCESS('Список товаров пуст.'))
