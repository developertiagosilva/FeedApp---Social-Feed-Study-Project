from django.urls import path
from .views import (
    PostListView, PostDetailView, 
    PostCreateView, PostUpdateView, PostDeleteView, login_view
)

urlpatterns = [
    path('', login_view, name='login'),
    path('feed/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/novo/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/deletar/', PostDeleteView.as_view(), name='post_delete'),
    path('login/', login_view, name='login'),
]