from django.shortcuts import render, redirect, get_object_or_404


from webapp.models import List, status_choices


def tasks_view(request):
    list = List.objects.all()
    return render(request, 'tasks.html', context={'lists': list})


def list_view(request, id):
    list = get_object_or_404(List, id=id)
    return render(request, 'list_view.html', context={'list': list})


def tasks_create_view(request):
    if request.method == "GET":
        return render(request, 'tasks_add_view.html', {'status': status_choices})
    elif request.method == "POST":
        description = request.POST.get('description')
        detailed_description = request.POST.get('detailed_description')
        status = request.POST.get('status')
        updated_at = request.POST.get('updated_at')
        if updated_at == '':
            updated_at = None

        list = List.objects.create(
            description=description,
            detailed_description=detailed_description,
            status=status,
            updated_at=updated_at
        )

        return redirect('task', id=list.id)

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


