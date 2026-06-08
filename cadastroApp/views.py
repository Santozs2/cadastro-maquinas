from django.shortcuts import render, redirect
from .models import Colaborador, Maquina
from .forms import ColaboradorForm, MaquinaForm
# Create your views here.

# INDEX

def home (request):
    return render(request, 'cadastroApp/index.html', {
        'titulo': 'Home',
    })

# DASHBOARD

def dashboard(request):
    maquinas = Maquina.objects.all()
    colaboradores = Colaborador.objects.all()
    busca_nome = request.GET.get('q', '')
    busca_numero_patrimonio = request.GET.get('numero_patrimonio', '')
    busca_modelo = request.GET.get('modelo', '')
    busca_setor = request.GET.get('setor', '')
    busca_colaborador = request.GET.get('colaborador', '')

    if busca_nome:
        maquinas = maquinas.filter(nome_maquina__icontains=busca_nome)
    if busca_numero_patrimonio:
        maquinas = maquinas.filter(numero_patrimonio__icontains=busca_numero_patrimonio)
    if busca_modelo:
        maquinas = maquinas.filter(modelo__icontains=busca_modelo)
    if busca_setor:
        maquinas = maquinas.filter(setor__icontains=busca_setor)
    if busca_colaborador:
        maquinas = maquinas.filter(colaborador_id=busca_colaborador)

    ordenacao = request.GET.get('sort', 'nome_maquina')
    valid_sorts = ['nome_maquina', '-nome_maquina', 'numero_patrimonio', '-numero_patrimonio', 'modelo', '-modelo', 'setor', '-setor', 'colaborador__nome', '-colaborador__nome']
    if ordenacao not in valid_sorts:
        ordenacao = 'nome_maquina'
    maquinas = maquinas.order_by(ordenacao)

    query_params = request.GET.copy()
    if 'sort' in query_params:
        del query_params['sort']
    url_base = request.path + '?' + query_params.urlencode() if query_params else request.path + '?'

    patrimonios = Maquina.objects.order_by('numero_patrimonio').values_list('numero_patrimonio', flat=True).distinct()
    modelos = Maquina.objects.order_by('modelo').values_list('modelo', flat=True).distinct()
    setores = Maquina.objects.order_by('setor').values_list('setor', flat=True).distinct()

    contexto = {
        'titulo': 'Dashboard',
        'colaboradores': colaboradores,
        'maquinas': maquinas,
        'ordenacao': ordenacao,
        'busca_nome': busca_nome,
        'busca_numero_patrimonio': busca_numero_patrimonio,
        'busca_modelo': busca_modelo,
        'busca_setor': busca_setor,
        'busca_colaborador': busca_colaborador,
        'patrimonios': patrimonios,
        'modelos': modelos,
        'setores': setores,
        'url_base': url_base,
    }
    return render(request, 'cadastroApp/dashboard_maquinas.html', contexto)

def dashboard_colaborador(request):
    colaboradores = Colaborador.objects.all()
    busca_nome = request.GET.get('q', '')
    busca_email = request.GET.get('email', '')
    busca_setor = request.GET.get('setor', '')

    if busca_nome:
        colaboradores = colaboradores.filter(nome__icontains=busca_nome)
    if busca_email:
        colaboradores = colaboradores.filter(email__icontains=busca_email)
    if busca_setor:
        colaboradores = colaboradores.filter(setor__icontains=busca_setor)

    ordenacao = request.GET.get('sort', 'nome')
    valid_sorts = ['nome', '-nome', 'email', '-email', 'setor', '-setor']
    if ordenacao not in valid_sorts:
        ordenacao = 'nome'
    colaboradores = colaboradores.order_by(ordenacao)

    query_params = request.GET.copy()
    if 'sort' in query_params:
        del query_params['sort']
    url_base = request.path + '?' + query_params.urlencode() if query_params else request.path + '?'

    setores = Colaborador.objects.order_by('setor').values_list('setor', flat=True).distinct()

    contexto = {
        'titulo': 'Dashboard | Colaboradores',
        'colaboradores': colaboradores,
        'ordenacao': ordenacao,
        'busca_nome': busca_nome,
        'busca_email': busca_email,
        'busca_setor': busca_setor,
        'url_base': url_base,
        'setores': setores,
    }
    return render(request, 'cadastroApp/dashboard_colaborador.html', contexto)


# MÁQUINAS

def maquina_listar(request):
    maquinas = Maquina.objects.all()
    ordenacao = request.GET.get('sort', 'nome_maquina')
    contexto = {
        'titulo': 'Lista de Máquinas',
        'maquinas': maquinas,
        'ordenacao': ordenacao,
        'criar_url': 'maquina_cadastrar',
        'editar_url': 'maquina_editar',
        'excluir_url': 'maquina_excluir',
    }
    return render(request, 'cadastroApp/model_list.html', contexto)

def maquina_cadastrar(request):
    if request.method == 'POST':
        form = MaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_maquinas')
    else:
        form = MaquinaForm()
    return render(request, 'cadastroApp/model_form.html', {
        'titulo': 'Cadastrar Máquina',
        'form': form,
    })

def maquina_editar(request, pk):
    maquina = Maquina.objects.get(pk=pk)
    if request.method == 'POST':
        form = MaquinaForm(request.POST, instance=maquina)
        if form.is_valid():
            form.save()
            return redirect('dashboard_maquinas')
    else:
        form = MaquinaForm(instance=maquina)
    return render(request, 'cadastroApp/model_edit.html', {
        'titulo': 'Editar Máquina',
        'form': form,
    })

def maquina_excluir(request, pk):
    maquina = Maquina.objects.get(pk=pk)
    if request.method == 'POST':
        maquina.delete()
        return redirect('dashboard_maquinas')
    return render(request, 'cadastroApp/model_delete.html', {
        'titulo': 'Excluir Máquina',
        'maquina': maquina,
    })


# COLABORADORES

def colaborador_listar(request):
    colaboradores = Colaborador.objects.all()
    ordenacao = request.GET.get('sort', 'nome')
    contexto = {
        'titulo': 'Lista de Colaboradores',
        'colaboradores': colaboradores,
        'ordenacao': ordenacao,
        'criar_url': 'model_form',
        'editar_url': 'model_edit',
        'excluir_url': 'model_delete',
    }
    return render(request, 'cadastroApp/model_list.html', contexto)

def colaborador_cadastrar(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_colaborador')
    else:
        form = ColaboradorForm()
    return render(request, 'cadastroApp/model_form.html', {
        'titulo': 'Cadastrar Colaborador',
        'form': form,
    })

def colaborador_editar(request, pk):
    colaborador = Colaborador.objects.get(pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('dashboard_colaborador')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'cadastroApp/model_edit.html', {
        'titulo': 'Editar Colaborador',
        'form': form,
    })


def colaborador_excluir(request, pk):
    colaborador = Colaborador.objects.get(pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('dashboard_colaborador')
    return render(request, 'cadastroApp/model_delete.html', {
        'titulo': 'Excluir Colaborador',
        'colaborador': colaborador,
    })



