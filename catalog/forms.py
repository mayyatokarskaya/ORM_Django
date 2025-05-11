from django import forms
from django.core.exceptions import ValidationError

from .models import Product

# Константа с запрещёнными словами
FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Исключаем поля, заполняемые автоматически
        exclude = ["created_at", "updated_at"]

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Название содержит запрещённое слово: «{word}»")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Описание содержит запрещённое слово: «{word}»")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
