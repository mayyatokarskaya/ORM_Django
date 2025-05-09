from django.views.generic import ListView, DetailView, View, TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core.paginator import Paginator


class HomePageView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "page_obj"
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ContactsView(View):
    def get(self, request):
        return render(request, "contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
