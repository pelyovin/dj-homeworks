from django.http import Http404
from django.shortcuts import render

from .models import Car, Sale


def cars_list_view(request):
    # получите список авто
    context = {'cars': Car.objects.all()}

    template_name = 'main/list.html'
    return render(request, template_name, context=context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        context = {'car': Car.objects.get(id=car_id)}
        template_name = 'main/details.html'
        return render(request, template_name, context=context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        context = {
            'car': Car.objects.get(id=car_id),
            'sales': Sale.objects.filter(car_id=car_id)
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context=context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
