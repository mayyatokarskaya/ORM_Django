from django.core.cache import cache

from .models import Product


def get_products_by_category(category_id, user=None):
    if (
        user
        and user.is_authenticated
        and user.has_perm("catalog.can_unpublish_product")
    ):
        cache_key = f"category_{category_id}_all_products"
        return cache.get_or_set(
            cache_key,
            lambda: list(Product.objects.filter(category_id=category_id)),
            timeout=300,
        )
    else:
        cache_key = f"category_{category_id}_published_products"
        return cache.get_or_set(
            cache_key,
            lambda: list(
                Product.objects.filter(category_id=category_id, status="published")
            ),
            timeout=300,
        )
