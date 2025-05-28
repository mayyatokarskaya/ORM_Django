from django.urls import path

from .views import (CategoryProductsView, ContactsView, HomePageView,
                    ProductCreateView, ProductDeleteView, ProductDetailView,
                    ProductUnpublishView, ProductUpdateView)

app_name = "catalog"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product/<int:pk>/unpublish/",
        ProductUnpublishView.as_view(),
        name="product_unpublish",
    ),
    path(
        "category/<int:category_id>/",
        CategoryProductsView.as_view(),
        name="category_products",
    ),
]
