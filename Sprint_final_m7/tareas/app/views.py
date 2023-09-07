from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


from app.models import Tareas
from datetime import datetime, time
from django.utils import timezone
from django.db.models import Q
from django.views.generic import DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy



from .forms import BuscarTarea, CrearTarea

estados ={
          1: 'Pendiente',
          2: 'En Progreso',
          3: 'Completada',
          4: 'Cancelada'
     }




# Create your views here.

def login_vista(request):
     #si ya está logeado
     if request.user.is_authenticated:
        messages.success(request, f'Cuenta activa : {request.user.username}')
        return redirect('dashboard')
   
     if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid(): # si el formulario de login es válido.
            user = authenticate(
               username = form.cleaned_data['username'],
               password = form.cleaned_data['password']
            )
            if user is not None:
               login(request, user)
               messages.success(request, f'Bienvenido {user.username}')
               return redirect('dashboard')
        else:
          for error in list(form.errors.values()):
               messages.error(request, error)
    
     form = AuthenticationForm()
     return render(request, 'login.html', {'form':form})
   


@login_required
def logout_vista(request):
    logout(request)
    messages.info(request, f'Sesión finalizada correctamente!')
    return redirect('index')

def index(request):
     return render(request, 'index.html') 

@login_required
def dashboard(request):
    
     now = datetime.now()
     end_of_day = (datetime.combine(now.date(), time.max))
    
     
     user = request.user.id

     # contadores de tareas pendientes --- estados[1]
     contTareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1]).count()
     pendientesVencHoy = Tareas.objects.filter(usuario_id=user, estado=estados[1], fecha_vencimiento__range=(now, end_of_day)).count()
     pendientesVencidas = Tareas.objects.filter(
          Q(usuario_id=user) &
          Q(estado=estados[1]) &
          Q(fecha_vencimiento__lt=now)
          ).count()
     
     # contadores de tareas En Progreso  --- estados[2]
     contTareasEnProgreso = Tareas.objects.filter(usuario_id=user, estado=estados[2]).count()
     enProgresoVencHoy = Tareas.objects.filter(usuario_id=user, estado=estados[2], fecha_vencimiento__range=(now, end_of_day)).count()
     enProgresoVencidas = Tareas.objects.filter(
          Q(usuario_id=user) &
          Q(estado=estados[2]) &
          Q(fecha_vencimiento__lt=now)
          ).count()
     
     # contadores de tareas Terminadas  --- estados[3]
     contTareasTerminadas = Tareas.objects.filter(usuario_id=user, estado=estados[3]).count()
     
     # contadores de tareas Canceladas  --- estados[3]
     contTareasCanceladas = Tareas.objects.filter(usuario_id=user, estado=estados[4]).count()

   

     
     data = {
          'contTareasPendientes' : contTareasPendientes,
          'pendientesVencHoy' : pendientesVencHoy,
          'pendientesVencidas' : pendientesVencidas,
          'contTareasEnProgreso' : contTareasEnProgreso,
          'enProgresoVencHoy' : enProgresoVencHoy,
          'enProgresoVencidas' : enProgresoVencidas,
          'contTareasTerminadas' : contTareasTerminadas,
          'contTareasCanceladas' : contTareasCanceladas,
      
          
     }


     return render(request, 'dashboard.html', data)     

@login_required     
def listaTareas(request):
     user = request.user.id
     if request.method == 'POST':
          form = BuscarTarea(request.POST)
          if form.is_valid(): 
               
               titulo = form.cleaned_data['titulo']
               descripcion = form.cleaned_data['descripcion']
               fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
               etiqueta = form.cleaned_data['etiqueta']
               observacion = form.cleaned_data['observacion']
               prioridad = form.cleaned_data['prioridad']
               
               

               # Crea un objeto Q vacío
               filtro = Q()

               # Verifica si cada campo de filtro está presente y agrega las condiciones correspondientes
               if titulo:
                    filtro |= Q(titulo=titulo)

               if descripcion:
                    filtro |= Q(descripcion=descripcion)

               if fecha_vencimiento:
                    filtro |= Q(fecha_vencimiento=fecha_vencimiento)

               if etiqueta:
                    filtro |= Q(etiqueta=etiqueta)

               if observacion:
                    filtro |= Q(observacion=observacion)

               if prioridad:
                    filtro |= Q(prioridad=prioridad)

               # Aplica el filtro en un solo queryset
               tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1]).filter(filtro).order_by('fecha_vencimiento').all()

               return render(request, 'listaTareas.html', {'tareasPendientes': tareasPendientes, 'form': form})


               # if titulo:
               #      tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1], titulo =titulo).order_by('fecha_vencimiento').all()
               # if descripcion:
               #      tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1], descripcion =descripcion).order_by('fecha_vencimiento').all()
               # if fecha_vencimiento:
               #      tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1], fecha_vencimiento =fecha_vencimiento).order_by('fecha_vencimiento').all()
               # if etiqueta:
               #      print(etiqueta)
               #      tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1], etiqueta =etiqueta).order_by('fecha_vencimiento').all()    
               # if observacion:
               #      tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1], observacion =observacion).order_by('fecha_vencimiento').all() 
               # if prioridad:
               #      tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1], prioridad =prioridad).order_by('fecha_vencimiento').all()  
       

               # return render(request, 'listaTareas.html', {'tareasPendientes': tareasPendientes, 'form':form})
          
     

     

     # tareas pendientes --- estados[1]
     tareasPendientes = Tareas.objects.filter(usuario_id=user, estado=estados[1]).order_by('fecha_vencimiento').all()
     
     
     # tareas En Progreso  --- estados[2]
     tareasEnProgreso = Tareas.objects.filter(usuario_id=user, estado=estados[2]).order_by('fecha_vencimiento').all()
     
     # tareas Terminadas  --- estados[3]
     tareasTerminadas = Tareas.objects.filter(usuario_id=user, estado=estados[3]).order_by('fecha_vencimiento').all()
     
     # tareas Canceladas  --- estados[3]
     tareasCanceladas = Tareas.objects.filter(usuario_id=user, estado=estados[4]).order_by('fecha_vencimiento').all()

     form = BuscarTarea()

     
     data = {
          'tareasPendientes' : tareasPendientes,
          'tareasEnProgreso' : tareasEnProgreso,
          'tareasTerminadas' : tareasTerminadas,
          'tareasCanceladas' : tareasCanceladas,  
          'form' : form
     }

     return render(request, 'listaTareas.html', data)

@login_required 
def crearTarea(request):
     if request.method == 'POST':
          form = CrearTarea(request.POST)
          if form.is_valid(): 
               

               fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
               print(fecha_vencimiento)
               zona_horaria_usuario = timezone.get_current_timezone()
               print(zona_horaria_usuario)
               form.save()
               return redirect('listaTareas')
     form =  CrearTarea() 
     return render(request, 'crearTarea.html', {'form':form})


@login_required
def completarTarea(request, pk):
    tarea = get_object_or_404(Tareas , pk=pk)
    tarea.estado = 'Completada'
    tarea.save()
    messages.success(request, 'Tarea marcada como completada!')
    return redirect('listaTareas')

     

class TareaDetailView(DetailView):
    model = Tareas
    template_name = 'tareaDetalle.html'
    context_object_name = 'Tarea'
     

class TareaDeleteView(DeleteView):
    model = Tareas
    success_url = reverse_lazy('listaTareas')
    
class TareaUpdateView(UpdateView):
    model = Tareas
    form_class = CrearTarea
    template_name = 'editarTarea.html'
    success_url = reverse_lazy('listaTareas')

