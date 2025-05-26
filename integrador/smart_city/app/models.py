from django.db import models

class Sensores(models.Model):
    # tipo de escolha para sensores
    sensor_CHOICES = [
        ('T', 'Temperatura'),
        ('L', 'Luminosidade'),
        ('U', 'Umidade'),
        ('C', 'Contador'),
    ]
    sensor = models.CharField(max_length=100,  choices=sensor_CHOICES, default='C' )
    mac_address = models.CharField(max_length=100)
    # tipos de escolhas para unidade de medida
    unidade_med_CHOICES = [
        ('°C', '°C'),
        ('lux', 'lux'),
        ('%', '%'),
        ('num', 'num'),
    ]

    unidade_med = models.CharField(max_length=3, choices=unidade_med_CHOICES, default='°C')
    latitude = models.FloatField()
    longitude = models.FloatField()
    # tipos de escolhas para status
    status_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]
    status = models.CharField(max_length=1, choices=status_CHOICES, default='A')

    # retornar o sensor
    def __str__(self):
        return self.sensor
    

class Ambientes(models.Model):
    #  codigo do ambiente
    sig = models.IntegerField()
    descricao = models.CharField(max_length=100)
    # numero de indentificação
    ni = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.sig


class Historico(models.Model):
    # chave estrangeira da class Sensores
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    # chave estrangeira da class Ambientes
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.IntegerField()
    
    def __str__(self):
        return self.sensor