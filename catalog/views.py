from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"page_obj": page_obj})


def contacts(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
