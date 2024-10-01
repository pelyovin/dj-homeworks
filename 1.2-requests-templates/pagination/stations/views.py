import csv

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open(settings.BUS_STATION_CSV) as file:
        data = list(csv.DictReader(file))
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': [i for i in page],
        'page': page,
    }
    return render(request, 'stations/index.html', context)
