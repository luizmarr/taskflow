
from django.urls import path
import tarefas.views as views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
]