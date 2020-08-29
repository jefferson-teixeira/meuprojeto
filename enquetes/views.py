from django.shortcuts import render
from enquetes.models import Enquete
# Create your views here.

def bemvindo(request):
    return render(request, 'bemvindo.html')    


def exibir(request, enquete_id):
    enquetes = {
        1: Enquete(1, 'Qual o seu nome?', '29/08/2020'),
        2: Enquete(2, 'Qual sua idade?', '29/08/2020'),
        3: Enquete(3, 'Qual sua cor favorita?', '29/08/2020')
    }

    enquete = enquetes[enquete_id]
    
    return render(request, 'enquete.html', {'enquete': enquete})