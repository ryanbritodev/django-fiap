from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        # Recebe os dados do formulário
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmacao_senha = request.POST['confirmacao-senha']
        # Validação dos campos
        if not nome.strip():
            messages.error(request, 'Nome não pode ficar em branco')
            return redirect('cadastro')
        if not sobrenome.strip():
            messages.error(request, 'Sobrenome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'E-mail não pode ficar em branco')
            return redirect('cadastro')
        if senha != confirmacao_senha:
            messages.error(request, 'Senha diferentes. Informe as mesmas senhas, por favor.')
            return redirect('cadastro')
        # Execução da chamada ao banco de dados
        User.objects.create_user(first_name=nome, last_name=sobrenome, email=email,
                                 username=f'{nome} {sobrenome}', password=senha)
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        # Recebe os dados do formulário
        email = request.POST['email']
        senha = request.POST['senha']

        # Validação dos campos
        if email == '' or senha == '':
            messages.error(request, 'E-mail e senha devem ser preenchidos')
            return redirect('login')

        # Verifica se o usuário existe
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Senha incorreta')
        else:
            messages.error(request, 'E-mail não encontrado')

    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
