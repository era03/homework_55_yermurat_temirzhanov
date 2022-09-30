from django import forms
from django.forms import CharField



class ToDo(forms.Form):
    description = CharField(max_length=50, required=True, label='Наименование')
    status = CharField(max_length=20, required=True, label='Статус')
    deadline = CharField(max_length=50, required=True, label='Дата окончания')
    full_description = CharField(max_length=500, required=True, label='Полное описание')
