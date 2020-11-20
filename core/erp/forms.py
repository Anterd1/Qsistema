from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField(label='asunto',max_length=100)
    mail = forms.EmailField(label='mail')
    mensaje = forms.CharField(label='mensaje')


