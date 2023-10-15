from django.core.management.base import BaseCommand
from myapp.models import Product  # Замените на вашу модель Product

class Command(BaseCommand):
    help = 'Добавление товаров в базу данных'

    def handle(self, *args, **kwargs):
        # Пример добавления товаров
        products_to_add = [
            {
                'name': 'Книга',
                'description': 'Житие бытие',
                'price': 8.00,
                'quantity': 1,
            },
            {
                'name': 'Телефон Харриксон',
                'description': 'Орехоколка обычная',
                'price': 2.00,
                'quantity': 1,
            },
            {
                'name': 'Мышь',
                'description': 'Декор в холодильник',
                'price': 6.00,
                'quantity': 1,
            },
        ]

        for product_data in products_to_add:
            product = Product(**product_data)
            product.save()

            self.stdout.write(self.style.SUCCESS(f'Товар "{product.name}" успешно добавлен в базу данных.'))
