from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


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

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request, 'Usuario ou Senha inválidos.')

    return render(request, 'posts/login.html')