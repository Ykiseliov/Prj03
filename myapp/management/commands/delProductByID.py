# Удаляем Товар по ID
# Пример:  python manage.py delProductsByID <product_id>

# from django.core.management.base import BaseCommand
# from myapp.models import Product  # Замените на вашу модель Product
#
# class Command(BaseCommand):
#     help = 'Удаление товара по ID'
#
#     def add_arguments(self, parser):
#         parser.add_argument('product_id', type=int, help='ID товара')
#
#     def handle(self, *args, **kwargs):
#         product_id = kwargs['product_id']
#
#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             self.stdout.write(self.style.ERROR('Товар с указанным ID не найден.'))
#             return
#
#         # Удаляем товар
#         product.delete()
#
#         self.stdout.write(self.style.SUCCESS(f'Товар с ID {product_id} успешно удален.'))

# Вариант удаления 2
# from django.core.management.base import BaseCommand
from myapp.models import Product  # Замените на вашу модель Product

# class Command(BaseCommand):
#     help = 'Удаление товара по ID'
#
#     def add_arguments(self, parser):
#         parser.add_argument('product_id', type=int, help='ID товара')
#
#     def handle(self, *args, **kwargs):
#         product_id = kwargs['product_id']
#
#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             self.stdout.write(self.style.ERROR('Товар с указанным ID не найден.'))
#             return
#
#         # Выводим информацию о товаре
#         self.stdout.write(f'ID товара: {product.id}')
#         self.stdout.write(f'Название товара: {product.name}')
#         self.stdout.write(f'Описание товара: {product.description}')
#         self.stdout.write(f'Цена товара: {product.price}')
#         self.stdout.write(f'Количество товара: {product.quantity}')
#
#         self.stdout.write(self.style.SUCCESS(f'Товар с ID {product_id} успешно удален.'))

# Вариант удаления 3

from django.core.management.base import BaseCommand
from myapp.models import Product  # Замените на вашу модель Product

class Command(BaseCommand):
    help = 'Удаление товара по ID и отображение всех имеющихся товаров'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='ID товара')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Товар с указанным ID не найден.'))
            return

        # Удаляем товар
        product.delete()

        self.stdout.write(self.style.SUCCESS(f'Товар с ID {product_id} успешно удален.'))

        # Отображаем все имеющиеся товары после удаления
        self.stdout.write('\nСписок всех имеющихся товаров:')
        products = Product.objects.all()
        for p in products:
            self.stdout.write(f'ID товара: {p.id}')
            self.stdout.write(f'Название товара: {p.name}')
            self.stdout.write(f'Описание товара: {p.description}')
            self.stdout.write(f'Цена товара: {p.price}')
            self.stdout.write(f'Количество товара: {p.quantity}')