from django.db import models

# Modelo de Jugadores
class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team_id = models.IntegerField()
    
# Modelos de Metricas
from django.db import models


class PhysicalMetrics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    speed = models.FloatField()
    agility = models.FloatField()
    strength = models.FloatField()
    endurance = models.FloatField()

class TechnicalMetrics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pass_accuracy = models.FloatField()
    shooting_accuracy = models.FloatField()
    ball_control = models.FloatField()