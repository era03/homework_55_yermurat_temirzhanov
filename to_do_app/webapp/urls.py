from django.urls import path
from webapp.views.base import index_view
from webapp.views.to_do import to_do_add, delete_to_do, detail_to_do, update_to_do, confirm_delete_to_do



urlpatterns = [
    path('', index_view, name='index'),
    path('add/', to_do_add, name='add_to_do'),
    path('delete/<int:pk>/', delete_to_do, name='delete_to_do'),
    path('delete/<int:pk>/confirm_delete', confirm_delete_to_do ,name='confirm_delete_to_do'),
    path('to_do/', index_view, name='to_do'),
    path('to_do/<int:pk>/', detail_to_do, name='detail_view'),
    path('to_do/<int:pk>/edit', update_to_do, name='update_to_do')
]