from random import sample
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Accommodation


def main(request):
    title = 'главная'

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    hot_accommodation = sample(list(list_of_accommodations), 1)[0]

    content = {
        'title': title,
        'hot_accommodation': hot_accommodation,
    }

    return render(request, 'mainapp/index.html', content)


def accommodations(request):
    title = 'размещение'

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }

    return render(request, 'mainapp/accommodations.html', content)


def accommodation(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, 'mainapp/accommodation_details.html', content)
