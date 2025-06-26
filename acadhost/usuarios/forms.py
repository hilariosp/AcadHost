
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Equipe
from projeto.models import Projeto

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'nome', 'idade', 'telefone', 'cpf', 'tipo', 'username', 'password1', 'password2'
        ]

class UsuarioEditForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'telefone', 'endereco', 'cpf', 'tipo']

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ['usuario', 'projeto', 'funcao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Opcional: filtra só usuários ativos, por exemplo
        self.fields['usuario'].queryset = Usuario.objects.filter(is_active=True)

        # Opcional: ordena os projetos por título
        self.fields['projeto'].queryset = Projeto.objects.order_by('titulo')

        # Rótulos mais amigáveis
        self.fields['usuario'].label = "Membro"
        self.fields['projeto'].label = "Projeto"
        self.fields['funcao'].label = "Função na equipe"