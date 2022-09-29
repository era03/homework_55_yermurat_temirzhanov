from django.shortcuts import render
from django.shortcuts import redirect
from webapp.models import ToDo

# Create your views here.

def index_view(request):
    to_do = ToDo.objects.all()
    context = {
        "to_do": to_do
    }
    return render(request, 'index.html', context=context)

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
    return redirect('/')

def delete_to_do(request):
    pk = request.GET.get('pk')
    to_do_delete = ToDo.objects.filter(pk=pk)
    to_do_delete.delete()
    return redirect('/')


def detail_to_do(request, pk):
    to_do = ToDo.objects.get(pk=pk)
    return render (request, 'to_do.html', context = {'to_do': to_do})

