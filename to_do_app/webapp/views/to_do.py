from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from webapp.models import ToDo



def to_do_add(request):
    if request.method == 'GET':
        return render(request, 'to_do_add.html')
    to_do_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'deadline': request.POST.get('deadline'),
        'full_description': request.POST.get('full_description')
    }
    to_do = ToDo.objects.create(**to_do_data)
    return redirect('detail_view', pk=to_do.pk)





def update_to_do(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        to_do.description = request.POST.get('description')
        to_do.status = request.POST.get('status')
        to_do.deadline = request.POST.get('deadline')
        to_do.full_description = request.POST.get('full_description')
        to_do.save()
    return render(request, 'update_to_do.html', context={'to_do': to_do})


def detail_to_do(request, pk):
    to_do = ToDo.objects.get(pk=pk)
    return render (request, 'to_do.html', context = {'to_do': to_do})


def delete_to_do(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    return render(request, 'to_do_confirm_delete.html', context={'to_do': to_do})


def confirm_delete_to_do(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    to_do.delete()
    return redirect('to_do')


