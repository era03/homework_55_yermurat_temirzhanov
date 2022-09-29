from django.contrib import admin
from webapp.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'deadline')
    list_filter = ('id', 'description', 'status', 'deadline')
    search_fields = ('description', 'status', 'deadline')
    fields = ('description', 'status', 'deadline')
    readonly_fields = ('id', 'deadline')

admin.site.register(ToDo, ToDoAdmin)