from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .forms import ProductForm
from .models import Product


class HomePageView(ListView):
    model = Product
    template_name = "home.html"
    paginate_by = 4

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.has_perm("catalog.can_unpublish_product"):
            return Product.objects.all()
        return Product.objects.filter(status="published")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.status == "draft" and not (
            user.is_authenticated and user.has_perm("catalog.can_unpublish_product")
        ):
            from django.http import Http404

            raise Http404("Продукт не найден.")
        return product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    # permission_required = 'catalog.change_product'
    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_moderator = request.user.groups.filter(name="Модератор продуктов").exists()
        if product.owner != request.user and not is_moderator:
            return HttpResponseForbidden(
                "Недостаточно прав для редактирования этого продукта."
            )
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

    permission_required = "catalog.delete_product"

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_moderator = request.user.groups.filter(name="Модератор продуктов").exists()
        if product.owner != request.user and not is_moderator:
            return HttpResponseForbidden(
                "Недостаточно прав для удаления этого продукта."
            )
        return super().dispatch(request, *args, **kwargs)


class ContactsView(View):
    def get(self, request):
        return render(request, "contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductUnpublishView(PermissionRequiredMixin, View):
    permission_required = "catalog.can_unpublish_product"

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.status = "draft"
        product.save()
        messages.success(request, "Публикация продукта отменена.")
        return redirect("catalog:product_detail", pk=product.pk)
