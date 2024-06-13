from django.shortcuts import render
from .models import Musik


def news_view(request):
    musik = Musik.objects.all()

    return render(request, 'app/index.html', {'musik': musik})


def news_detail(request, pk):
    musik = Musik.objects.get(id=pk)

    return render(request, 'app/news_detail.html', {'musik': musik})
