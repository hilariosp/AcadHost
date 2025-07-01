from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Usuario # Importa o modelo de usuário personalizado
from .forms import UsuarioForm, UsuarioEditForm # Importa os formulários de usuário personalizados

# USUARIO CRUD

@login_required
@permission_required('usuarios.view_usuario', raise_exception=True) # Assumindo permissão view_usuario
def index(request):
    usuarios = Usuario.objects.all().order_by('nome') # Ordena por nome
    return render(request, 'usuarios/index.html', {'usuarios': usuarios})

def add(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # O método save no modelo Usuario (que você atualizou anteriormente)
            # lida com a atribuição de grupo com base no 'tipo'.
            return redirect('usuarios_index')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/add.html', {'form': form})

@login_required
@permission_required('usuarios.view_usuario', raise_exception=True) # Assumindo permissão view_usuario
def detail(request, id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)
    return render(request, 'usuarios/detail.html', {'usuario': usuario})

@login_required
@permission_required('usuarios.change_usuario', raise_exception=True)
def update(request, id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios_index')
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'usuarios/update.html', {'form': form})

@login_required
@permission_required('usuarios.delete_usuario', raise_exception=True)
def delete(request, id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)
    usuario.delete()
    return redirect('usuarios_index')

