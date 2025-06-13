from django.shortcuts import render, get_object_or_404
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'mix/home.html', {'produtos': produtos})

def detalhe(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'mix/detalhe.html', {'produto': produto})
