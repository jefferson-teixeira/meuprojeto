from django.shortcuts import render
from enquetes.models import Enquete
# Create your views here.

def bemvindo(request):
    return render(request, 'bemvindo.html')    


def exibir(request, enquete_id):
    e = Enquete.objects.get(id=enquete_id)
    return render(request, 'enquete.html', {'enquete': e})