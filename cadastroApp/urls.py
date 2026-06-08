from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard_maquinas/', views.dashboard, name='dashboard_maquinas'),
    path('dashboard_colaboradores/', views.dashboard_colaborador, name='dashboard_colaborador'),
    path('maquinas/', views.maquina_listar, name='maquina_listar'),
    path('maquinas/cadastrar/', views.maquina_cadastrar, name='maquina_cadastrar'),
    path('maquinas/listar/', views.maquina_listar, name='maquina_listar'),
    path('maquinas/editar/<int:pk>/', views.maquina_editar, name='maquina_editar'),
    path('maquinas/excluir/<int:pk>/', views.maquina_excluir, name='maquina_excluir'),
    path('colaboradores/', views.colaborador_listar, name='colaborador_listar'),
    path('colaboradores/cadastrar/', views.colaborador_cadastrar, name='colaborador_cadastrar'),
    path('colaboradores/listar/', views.colaborador_listar, name='colaborador_listar'),
    path('colaboradores/editar/<int:pk>/', views.colaborador_editar, name='colaborador_editar'),
    path('colaboradores/excluir/<int:pk>/', views.colaborador_excluir, name='colaborador_excluir'),
]