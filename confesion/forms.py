from django import forms
from confesion.models import Confesion, Comentario

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('contenido',)

class ConfesionForm(forms.ModelForm):

    class Meta:
        model = Confesion
        fields = ('nombre', 'edad', 'sexo', 'contenido',)