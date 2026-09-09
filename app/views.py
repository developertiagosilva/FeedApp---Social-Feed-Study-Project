from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Curtida


# READ ALL - Lista de posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


# READ ONE - Detalhe de um post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


# CREATE - Criar novo post
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['titulo', 'conteudo']


# UPDATE - Editar post existente
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['titulo', 'conteudo']


# DELETE - Remover post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


# AUTHENTICATION - Login
def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request, 'Usuário ou Senha inválidos.')

    return render(request, 'posts/login.html')


# AUTHENTICATION - Cadastro de Usuário
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático
            return redirect('post_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'posts/signup.html', {'form': form})


# REAÇÕES - Curtir/Descurtir Post
@login_required
def curtir_post_view(request, pk, tipo):
    post = get_object_or_404(Post, pk=pk)
    
    tipo_map = {
        'fogo': 'FOGO',
        'coracao': 'CORACAO'
    }
    
    tipo_enum = tipo_map.get(tipo)
    if tipo_enum:
        curtida_existente = Curtida.objects.filter(post=post, usuario=request.user, tipo=tipo_enum).first()
        
        if curtida_existente:
            curtida_existente.delete()  # Remove se já existia (toggle)
        else:
            Curtida.objects.create(post=post, usuario=request.user, tipo=tipo_enum)
            
    return redirect('post_list')



def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta.")
    return redirect('login')