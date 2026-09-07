from django.db import models
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    # Define para onde redirecionar após criar/editar
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})