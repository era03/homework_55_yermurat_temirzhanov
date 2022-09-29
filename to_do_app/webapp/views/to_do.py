from django.shortcuts import render
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


def delete_to_do(request):
    pk = request.GET.get('pk')
    to_do_delete = ToDo.objects.filter(pk=pk)
    to_do_delete.delete()
    return redirect('to_do')


def detail_to_do(request, pk):
    to_do = ToDo.objects.get(pk=pk)
    return render (request, 'to_do.html', context = {'to_do': to_do})
