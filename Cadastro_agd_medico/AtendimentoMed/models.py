from django.db import models

class Medico(models.Model): 
    nome = models.CharField(max_length=100)
    especializacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Paciente(models.Model): 
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class ConsultaMarcada(models.Model): 
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente =  models.ForeignKey(Paciente, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    
    def __str__(self):
        return f"{self.paciente} com {self.medico} em {self.data_hora}"