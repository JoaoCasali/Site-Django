from django.shortcuts import render


def index(request):
    alunos = {
        1: 'Lirinha',
        2: 'Felipe',
        3: 'Marcos'
    }

    dados = {
        'nome_do_aluno': alunos
    }

    return render(request, 'index.html', dados)


def aluno(request):
    return render(request, 'aluno.html')
