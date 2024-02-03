from django import forms

class MiFormulario(forms.Form):
    desde = forms.IntegerField(label='Ingresar desde')
    hasta = forms.IntegerField(label='Ingresar hasta')
