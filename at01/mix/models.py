from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    detalhes = models.TextField()
    imagens = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome
