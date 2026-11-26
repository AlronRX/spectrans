from django.shortcuts import render
from .forms import OrderForm

def order_form_view(request):
    # Создаем пустую форму для отображения на сайте
    form = OrderForm()
    # Передаем её в шаблон (второй аргумент - это словарь с данными)
    return render(request, 'orders/order_form.html', {'form': form})