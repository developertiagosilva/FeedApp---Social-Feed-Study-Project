from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

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