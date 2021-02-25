from django.shortcuts import render

# Create your views here.
from webapp.models import List

def list_view(request):
    list = List.objects.all()
    return render(request, 'list.html', context={'lists': list})

