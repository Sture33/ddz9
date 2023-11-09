from django.shortcuts import render
from app9.models import Games


# Create your views here.
def start_page(request):
    context = {'games': Games.objects.all()}
    return render(request,'index.html', context=context)

def detail(request, pk):
    game = Games.objects.get(pk=pk)
    context = {'game': game}
    return render(request, 'detail.html', context=context)