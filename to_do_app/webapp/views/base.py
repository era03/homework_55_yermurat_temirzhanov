from django.shortcuts import render
from django.shortcuts import redirect
from webapp.models import ToDo



def index_view(request):
    to_do = ToDo.objects.all()
    context = {
        "to_do": to_do
    }
    return render(request, 'index.html', context=context)