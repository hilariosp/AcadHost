from django import forms
from .models import Projeto, Tag, ProjetoTag

class ProjetoForm(forms.ModelForm):
    # Define explicitamente o campo 'tags' e ordena seu queryset
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by('nome'), # AQUI ESTÁ A ORDENAÇÃO!
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        required=False # Permite que projetos não tenham tags
    )

    class Meta:
        model = Projeto
        fields = [
            'nome',
            'introducao',
            'resumo',
            'referencial_teorico',
            'desenvolvimento',
            'resultados',
            'conclusao',
            'referencias',
            'tags', 
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'introducao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'resumo': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'referencial_teorico': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'desenvolvimento': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'resultados': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'conclusao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'referencias': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
        }

class ProjetoTagForm(forms.ModelForm):
    class Meta:
        model = ProjetoTag
        fields = ['projeto', 'tag']
        widgets = {
            'projeto': forms.Select(attrs={'class': 'form-control'}),
            'tag': forms.Select(attrs={'class': 'form-control'}),
        }