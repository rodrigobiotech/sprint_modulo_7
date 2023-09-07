from django.urls import path
from .views import index, login_vista, logout_vista, dashboard, listaTareas, crearTarea, TareaDeleteView, TareaUpdateView, TareaDetailView, completarTarea

urlpatterns = [
    path('', index ,name='index'),
    path('login/', login_vista, name='login'),
    path('logout/', logout_vista, name='logout'),
    path('dashboard', dashboard ,name='dashboard'),
    path('listaTareas', listaTareas ,name='listaTareas'),
    path('crearTarea', crearTarea ,name='crearTarea'),
    path('eliminarTarea/<pk>/', TareaDeleteView.as_view(), name='eliminarTarea'),
    path('editarTarea/<pk>/', TareaUpdateView.as_view(), name='editarTarea'),
    path('verTarea/<pk>/', TareaDetailView.as_view(), name='verTarea'),
    path('completarTarea/<pk>/', completarTarea, name='completarTarea'),
    
]
