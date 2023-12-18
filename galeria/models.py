from datetime import datetime

from django.db import models

from django.contrib.auth.models import User


class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galaxia"),
        ("PLANETA", "Planeta"),
    ]
    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    legenda = models.CharField('Legenda', max_length=150, null=False, blank=False)
    categoria = models.CharField('Categoria', max_length=100, choices=OPCOES_CATEGORIA, default="#")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    # Conseguirei fazer upload de fotos, o blank diz que posso cadastra e não colocar nenhuma img.
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return self.nome
