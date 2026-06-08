from django.db import models



class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    setor = models.CharField(max_length=20)
    maquina = models.ForeignKey('Maquina', on_delete=models.SET_NULL, null=True, blank=True, related_name='colaborador_responsavel')

    def __str__(self):
        return self.nome

class Maquina(models.Model):
    nome_maquina = models.CharField(max_length=100)
    numero_patrimonio = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    setor = models.CharField(max_length=20)
    colaborador = models.OneToOneField('Colaborador', on_delete=models.SET_NULL, null=True, blank=True, related_name='maquina_atribuidas')

    def __str__(self):
        return self.nome_maquina
    