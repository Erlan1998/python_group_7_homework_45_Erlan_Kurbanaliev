from django.shortcuts import render, redirect, get_object_or_404


from webapp.models import List, status_choices
from webapp.froms import ListForm


def tasks_view(request):
    list = List.objects.all()
    return render(request, 'tasks.html', context={'lists': list})


def list_view(request, id):
    list = get_object_or_404(List, id=id)
    return render(request, 'list_view.html', context={'list': list})


def tasks_create_view(request):
    if request.method == "GET":
        form = ListForm
        return render(request, 'tasks_add_view.html', context={'form': form})
    elif request.method == "POST":
        form = ListForm(data=request.POST)
        if form.is_valid():
            list = List.objects.create(
                description=form.cleaned_data.get('description'),
                detailed_description = form.cleaned_data.get('detailed_description'),
                status = form.cleaned_data.get('status'),
                updated_at = form.cleaned_data.get('updated_at')
            )
            return redirect('task', id=list.id)
        return render(request, 'tasks_add_view.html', context={'form': form})

def list_update_view(request, id):
    list = get_object_or_404(List, id=id)
    if request.method == 'GET':
        return render(request, 'list_update.html', context={'list': list, "status": status_choices})
    elif request.method == 'POST':
        list.description = request.POST.get('description')
        list.detailed_description = request.POST.get('detailed_description')
        list.status = request.POST.get('status')
        list.updated_at = request.POST.get('updated_at')
        list.save()
        return redirect('task', id=list.id)

def list_delete_view(request, id):
    list = get_object_or_404(List, id=id)
    if request.method == 'GET':
        return render(request, 'list_delete.html', context={'list': list})
    elif request.method == 'POST':
        list.delete()
    return redirect('index_tasks')


