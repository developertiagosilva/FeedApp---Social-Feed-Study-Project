from django.urls import path
from .views import (
    PostListView, PostDetailView, 
    PostCreateView, PostUpdateView, PostDeleteView, login_view, signup_view, curtir_post_view, logout_view
)

urlpatterns = [
    path('', login_view, name='login'),
    path('cadastrar/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('feed/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/novo/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/deletar/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/curtir/<str:tipo>/', curtir_post_view, name='curtir_post'),
]