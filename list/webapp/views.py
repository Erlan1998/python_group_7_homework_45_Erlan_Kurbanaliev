from django.shortcuts import render

# Create your views here.
from webapp.models import List

def tasks_view(request):
    list = List.objects.all()
    return render(request, 'tasks.html', context={'lists': list})

def list_view(request):

    list_id = request.GET.get('id')
    list = List.objects.get(id=list_id)
    return render(request, 'list_view.html', context={'list': list})

