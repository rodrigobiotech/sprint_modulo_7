from django import forms
from .models import Tareas, User

class CrearTarea(forms.ModelForm):
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Widget personalizado para el campo descripcion
        max_length=256,
        # required=False  # Opcional, según tus necesidades
    )
    fecha_vencimiento = forms.DateTimeField(
        label='Fecha de Vencimiento',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Formato de entrada para el campo
    )
    estado = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'custom-select'}),  # Widget personalizado para el campo estado
        choices=Tareas.ESTADO_CHOICES  # Utilizamos las opciones definidas en el modelo Tareas
    )
    etiqueta = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'custom-select'}),  # Widget personalizado para el campo etiqueta
        choices=Tareas.ETIQUETA_CHOICES  # Utilizamos las opciones definidas en el modelo Tareas
    )
    usuario = forms.ModelChoiceField(queryset=User.objects.all())
    observacion = forms.CharField(
         widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Widget personalizado para el campo descripcion
        max_length=256,
        # required=False  # Opcional, según tus necesidades
        )
    prioridad = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'custom-select'}),  # Widget personalizado para el campo prioridad
        choices=Tareas.PRIORIDAD_CHOICES  # Utilizamos las opciones definidas en el modelo Tareas
    )
    
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'estado', 'etiqueta', 'usuario',  'observacion', 'prioridad']
    
class BuscarTarea(forms.ModelForm):
    titulo = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}),  # Widget personalizado para el campo descripcion
        max_length=256,
        required=False  # Opcional, según tus necesidades
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}),  # Widget personalizado para el campo descripcion
        max_length=256,
        required=False  # Opcional, según tus necesidades
    )
    fecha_vencimiento = forms.DateTimeField(
        label='Fecha de Vencimiento',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Formato de entrada para el campo
        required=False
    )

    etiqueta = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'custom-select'}),  # Widget personalizado para el campo etiqueta
        choices=Tareas.ETIQUETA_CHOICES,  # Utilizamos las opciones definidas en el modelo Tareas
        required=False
    )
    observacion = forms.CharField(
         widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}),  # Widget personalizado para el campo descripcion
        max_length=256,
        required=False  # Opcional, según tus necesidades
        )
    prioridad = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'custom-select'}),  # Widget personalizado para el campo prioridad
        choices=Tareas.PRIORIDAD_CHOICES,  # Utilizamos las opciones definidas en el modelo Tareas
        required=False
    )
    
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'etiqueta',  'observacion', 'prioridad']
   