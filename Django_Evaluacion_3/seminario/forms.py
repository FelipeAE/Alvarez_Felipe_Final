from django import forms
from .models import Inscrito, Institucion
from django.core import validators

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'telefono',  'institucion', 'estado', 'observacion'] #'fecha_inscripcion',
        labels = {
            'nombre': 'Nombre',
            'telefono': 'Teléfono',
            'fecha_inscripcion': 'Fecha de Inscripción',
            'institucion': 'Institución',
            'estado': 'Estado',
            'observacion': 'Observación',
        }
        
    Estado = [('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')]
    
    nombre = forms.CharField(validators=[validators.MinLengthValidator(3, "El nombre debe tener un minimo de 3 caracteres"), validators.MaxLengthValidator(100, "El nombre debe tener un maximo de 100 caracteres")], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su teléfono'} ))
    # fecha_inscripcion = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la fecha de inscripción', 'type':'date' }))
    institucion = forms.ModelChoiceField(queryset=Institucion.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    estado = forms.ChoiceField(choices=Estado, widget=forms.Select(attrs={'class':'form-select'}))
    observacion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese su observación', 'rows':'3'}))
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono[0] != '9' or telefono.isdigit() == False:
            raise forms.ValidationError('El teléfono debe empezar con 9 y solo debe contener números')
        return telefono
    
    # def clean_fecha_inscripcion(self):
    #     fecha_inscripcion = self.cleaned_data['fecha_inscripcion']
    #     if fecha_inscripcion.year < 2020:
    #         raise forms.ValidationError('El año de la fecha de inscripción debe ser mayor o igual a 2020')
    #     return fecha_inscripcion
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not all(x.isalpha() or x.isspace() for x in nombre.split()):
            raise forms.ValidationError('El nombre solo debe contener letras y espacios')
        return nombre

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }
        
    nombre = forms.CharField(validators=[validators.MinLengthValidator(3, "El nombre debe tener un minimo de 3 caracteres"), validators.MaxLengthValidator(200, "El nombre debe tener un maximo de 200 caracteres")], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el nombre de la institución'}) )
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not all(x.isalpha() or x.isspace() for x in nombre.split()):
            raise forms.ValidationError('El nombre solo debe contener letras y espacios')
        return nombre
