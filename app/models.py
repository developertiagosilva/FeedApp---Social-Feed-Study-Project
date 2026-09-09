from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    # Define para onde redirecionar após criar/editar
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    # Contadores de curtidas para o template
    def total_fogo(self):
        return self.curtidas.filter(tipo='FOGO').count()

    def total_coracao(self):
        return self.curtidas.filter(tipo='CORACAO').count()


class Curtida(models.Model):
    TIPO_REACAO = (
        ('FOGO', '🔥'),
        ('CORACAO', '❤️'),
    )
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='curtidas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_REACAO)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Garante que o mesmo usuário não curta o mesmo post com o mesmo emoji 2 vezes
        unique_together = ('post', 'usuario', 'tipo')

    def __str__(self):
        return f"{self.usuario.username} react {self.tipo} no post {self.post.id}"