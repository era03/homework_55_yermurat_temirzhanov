from email.policy import default
from django.db import models

# Create your models here.
class ToDo(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.TextField(max_length=200, null=False, blank=False, default='new', verbose_name='Статус')
    deadline = models.TextField(verbose_name='Дата выполнения', null=True, blank=True, default='No deadline')
    full_description = models.TextField(max_length=200, null=False, blank=False, default='No description', verbose_name='Подробное описание')


    def __str__(self) -> str:
        return f"{self.description} - {self.status} - {self.deadline}"