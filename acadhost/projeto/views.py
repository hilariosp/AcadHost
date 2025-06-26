from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Projeto, Tag, ProjetoTag
from .forms import ProjetoForm, TagForm, ProjetoTagForm

# PROJETO

@login_required
def index(request):
    projetos = Projeto.objects.all()
    tags = Tag.objects.all().order_by('nome')
    return render(request, 'projeto/index.html', {'projetos': projetos, 'tags': tags})

@login_required
def detail(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    return render(request, 'projeto/detail.html', {'projeto': projeto})

@login_required
@permission_required('projeto.add_projeto', raise_exception=True)
def add(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.autor = request.user  # assume que o autor é o usuário logado
            projeto.save()
            form.save_m2m() 
            return HttpResponseRedirect('/projeto/')
    else:
        form = ProjetoForm()
    return render(request, 'projeto/add.html', {'form': form})

@login_required
@permission_required('projeto.change_projeto', raise_exception=True)
def update(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projeto/')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projeto/update.html', {'form': form})

@login_required
@permission_required('projeto.delete_projeto', raise_exception=True)
def delete(request, id_projeto):
    Projeto.objects.filter(id=id_projeto).delete()
    return HttpResponseRedirect('/projeto/')

# TAG

@login_required
def tag_index(request):
    tags = Tag.objects.all()
    return render(request, 'projeto/tag_index.html', {'tags': tags})

@login_required
@permission_required('projeto.add_tag', raise_exception=True)
def tag_add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projeto/tags/')
    else:
        form = TagForm()
    return render(request, 'projeto/tag_add.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from usuarios.models import Usuario 
from .models import Projeto, Tag, ProjetoTag
from .forms import ProjetoForm, TagForm, ProjetoTagForm

# PROJETO

@login_required
def index(request):
    projetos = Projeto.objects.all()
    tags = Tag.objects.all().order_by('nome')
    return render(request, 'projeto/index.html', {'projetos': projetos, 'tags': tags})

@login_required
def detail(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    return render(request, 'projeto/detail.html', {'projeto': projeto})

@login_required
@permission_required('projeto.add_projeto', raise_exception=True)
def add(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.autor = request.user 
            projeto.save()
            form.save_m2m() 
            return HttpResponseRedirect('/projeto/')
    else:
        form = ProjetoForm()
    return render(request, 'projeto/add.html', {'form': form})

@login_required
@permission_required('projeto.change_projeto', raise_exception=True)
def update(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projeto/')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projeto/update.html', {'form': form})

@login_required
@permission_required('projeto.delete_projeto', raise_exception=True)
def delete(request, id_projeto):
    Projeto.objects.filter(id=id_projeto).delete()
    return HttpResponseRedirect('/projeto/')

# TAG

@login_required
def tag_index(request):
    tags = Tag.objects.all().order_by('nome') # Garante que as tags sempre venham ordenadas alfabeticamente na listagem
    return render(request, 'projeto/tag_index.html', {'tags': tags})

@login_required
@permission_required('projeto.add_tag', raise_exception=True)
def tag_add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projeto_index') 
    else:
        form = TagForm()
    return render(request, 'projeto/tag_add.html', {'form': form})

@login_required
def tag_detail(request, id_tag):
    tag = get_object_or_404(Tag, id=id_tag)
    return render(request, 'projeto/tag_detail.html', {'tag': tag})

@login_required
@permission_required('projeto.change_tag', raise_exception=True) # <-- Permissão adicionada
def tag_update(request, id_tag):
    tag = get_object_or_404(Tag, id=id_tag)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('projeto_index') 
    else:
        form = TagForm(instance=tag)
    return render(request, 'projeto/tag_update.html', {'form': form})

@login_required
@permission_required('projeto.delete_tag', raise_exception=True) # <-- Permissão adicionada
def tag_delete(request, id_tag):
    Tag.objects.filter(id=id_tag).delete() 
    return redirect('projeto_index')

