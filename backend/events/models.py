from django.db import models

# Create your models here.
class events(models.Model):
    titulos = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()
    tipo = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ['data'] #lista primeiro o mais recente 

    def __str__(self):
        return f'Título: {self.titulos} | Tipo: {self.tipo} | Data: {self.data} | Localização: ({self.latitude}, {self.longitude})'