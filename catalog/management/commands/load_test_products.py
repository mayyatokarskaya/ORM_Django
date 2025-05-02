from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Загружает тестовые продукты из фикстур с предварительной очисткой БД"

    def handle(self, *args, **options):
        # 1. Очистка существующих данных
        self.stdout.write("Удаление существующих продуктов и категорий...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        # 2. Загрузка фикстур
        self.stdout.write("Загрузка тестовых данных из фикстур...")

        try:
            # Сначала загружаем категории
            call_command("loaddata", "categories.json")

            # Затем загружаем продукты
            call_command("loaddata", "products.json")

            self.stdout.write(
                self.style.SUCCESS("✅ Тестовые данные успешно загружены!")
            )

            # Проверяем связи
            self.check_relations()

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Ошибка загрузки данных: {str(e)}"))

    def check_relations(self):
        """Проверка корректности связей между продуктами и категориями"""
        products_without_category = Product.objects.filter(category__isnull=True)
        if products_without_category.exists():
            self.stdout.write(
                self.style.WARNING("⚠️ Обнаружены продукты без категории!")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "✅ Все продукты имеют корректные связи с категориями"
                )
            )
