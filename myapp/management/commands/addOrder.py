# Команда для добавления заказанных товаров клиенту  ID у которого 1

from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order  # Замените на ваши модели

class Command(BaseCommand):
    help = 'Добавление заказанных товаров клиенту'

    def handle(self, *args, **kwargs):
        # Найдем клиента с ID 1 (замените на нужный ID)
        try:
            client = Client.objects.get(id=1)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR('Клиент с указанным ID не найден.'))
            return

        # Создаем заказ
        order = Order.objects.create(client=client, total_amount=0)  # Может потребоваться указать корректное значение total_amount

        # Добавляем товары в заказ (пример)
        # Замените этот код на свой способ добавления товаров к заказу
        products_to_add = [4, 5, 6]  # ID товаров для добавления
        products = Product.objects.filter(id__in=products_to_add)

        # Добавляем выбранные товары к заказу
        for product in products:
            order.products.add(product)

        # Рассчитываем общую сумму заказа (пример, предполагается, что у товаров есть поле price)
        total_amount = sum(product.price for product in products)
        order.total_amount = total_amount
        order.save()

        self.stdout.write(self.style.SUCCESS(f'Заказ успешно создан для клиента {client.name}.'))
