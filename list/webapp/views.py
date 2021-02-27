from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.
from webapp.models import List, status_choices


def tasks_view(request):
    list = List.objects.all()
    return render(request, 'tasks.html', context={'lists': list})


def list_view(request, id):
    list = List.objects.get(id=id)
    return render(request, 'list_view.html', context={'list': list})


def tasks_create_view(request):
    if request.method == "GET":
        return render(request, 'tasks_add_view.html', {'status': status_choices})
    elif request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get('status')
        updated_at = request.POST.get('updated_at')
        if updated_at == '':
            updated_at = None

        list = List.objects.create(
            description=description,
            status=status,
            updated_at=updated_at
        )
        uri = reverse('task', kwargs={"id": list.id})
        return HttpResponseRedirect(uri)
