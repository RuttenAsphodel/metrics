# players/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from .models import PhysicalMetrics, TechnicalMetrics
import math
import plotly.graph_objects as go


def inicio(request):
    return render(request, 'inicio.html')
# Vistas para Jugadores
def player_list(request):
    players = Player.objects.all()
    return render(request, 'players/list.html', {'players': players})

def player_detail(request, player_id):

    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'players/details.html', {'player': player})

def player_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        team_id = request.POST['team_id']
        player = Player.objects.create(name=name, position=position, team_id=team_id)
        return redirect('player_detail', player_id=player.id)
    return render(request, 'players/create.html')

def player_update(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        player.name = request.POST['name']
        player.position = request.POST['position']
        player.team_id = request.POST['team_id']
        player.save()
        return redirect('player_detail', player_id=player.id)
    return render(request, 'players/update.html', {'player': player})

def player_delete(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'players/delete.html', {'player': player})

# Vistas para Metricas 

def metrics_create(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        speed = request.POST['speed']
        agility = request.POST['agility']
        strength = request.POST['strength']
        endurance = request.POST['endurance']
        pass_accuracy = request.POST['pass_accuracy']
        shooting_accuracy = request.POST['shooting_accuracy']
        ball_control = request.POST['ball_control']
        physical_metrics = PhysicalMetrics.objects.create(player=player, speed=speed, agility=agility, strength=strength, endurance=endurance)
        technical_metrics = TechnicalMetrics.objects.create(player=player, pass_accuracy=pass_accuracy, shooting_accuracy=shooting_accuracy, ball_control=ball_control)
        return redirect('resumen_performance', player_id=player.id)
    return render(request, 'metrics/create.html', {'player': player})

def metrics_update(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    physical_metrics = PhysicalMetrics.objects.filter(player=player).first()
    technical_metrics = TechnicalMetrics.objects.filter(player=player).first()
    if request.method == 'POST':
        physical_metrics.speed = request.POST['speed']
        physical_metrics.agility = request.POST['agility']
        physical_metrics.strength = request.POST['strength']
        physical_metrics.endurance = request.POST['endurance']
        technical_metrics.pass_accuracy = request.POST['pass_accuracy']
        technical_metrics.shooting_accuracy = request.POST['shooting_accuracy']
        technical_metrics.ball_control = request.POST['ball_control']
        physical_metrics.save()
        technical_metrics.save()
        return redirect('resumen_performance', player_id=player.id)
    return render(request, 'metrics/update.html', {'player': player, 'physical_metrics': physical_metrics, 'technical_metrics': technical_metrics})

def metrics_delete(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    physical_metrics = PhysicalMetrics.objects.filter(player=player).first()
    technical_metrics = TechnicalMetrics.objects.filter(player=player).first()
    if request.method == 'POST':
        physical_metrics.delete()
        technical_metrics.delete()
        return redirect('resumen_performance', player_id=player.id)
    return render(request, 'metrics/delete.html', {'player': player})


def calculate_key_metrics(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    physical_metrics = PhysicalMetrics.objects.filter(player=player).first()
    technical_metrics = TechnicalMetrics.objects.filter(player=player).first()

    # Calcular métricas clave utilizando funciones exponenciales
    sprint_speed = 10 * math.exp(0.05 * physical_metrics.speed)
    vertical_jump = 50 * math.exp(0.02 * physical_metrics.strength)
    shot_power = 60 * math.exp(0.03 * physical_metrics.strength)
    pass_accuracy = 35 * math.exp(0.01 * technical_metrics.pass_accuracy)
    shooting_accuracy = 15 * math.exp(0.02 * technical_metrics.shooting_accuracy)

    return  {
        'player': player,
        'sprint_speed': sprint_speed,
        'vertical_jump': vertical_jump,
        'shot_power': shot_power,
        'pass_accuracy': pass_accuracy,
        'shooting_accuracy': shooting_accuracy
    }
    
def metrics_detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    physical_metrics = PhysicalMetrics.objects.filter(player=player).first()
    technical_metrics = TechnicalMetrics.objects.filter(player=player).first()
    return  {
        'player': player,
        'physical_metrics': physical_metrics,
        'technical_metrics': technical_metrics,
    }
    

def optimize_player_position(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    physical_metrics = PhysicalMetrics.objects.filter(player=player).first()
    technical_metrics = TechnicalMetrics.objects.filter(player=player).first()

    # Lógica para determinar la posición óptima
    if physical_metrics.speed > 90 and physical_metrics.agility > 85:
        recommended_position = 'Lateral'
    elif physical_metrics.strength > 80 and technical_metrics.shooting_accuracy > 80:
        recommended_position = 'Atacante'
    elif physical_metrics.endurance > 90 and technical_metrics.pass_accuracy > 85:
        recommended_position = 'Mediocampista'
    else:
        recommended_position = 'Defensa'

    return {
        'player': player,
        'recommended_position': recommended_position
    }
    
def player_performance_chart(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    physical_metrics = PhysicalMetrics.objects.filter(player=player).first()
    technical_metrics = TechnicalMetrics.objects.filter(player=player).first()

    # Crear el gráfico de radar
    fig = go.Figure(data=go.Scatterpolar(
        r=[physical_metrics.speed, physical_metrics.agility, physical_metrics.strength, physical_metrics.endurance,
           technical_metrics.pass_accuracy, technical_metrics.shooting_accuracy, technical_metrics.ball_control],
        theta=['Velocidad', 'Agilidad', 'Fuerza', 'Resistencia', 'Pases', 'Disparo', 'Control'],
        fill='toself'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=False,
                range=[0, 100]
            )),
        showlegend=False
    )
    chart_div = fig.to_html(full_html=False)

    return  {
        'player': player,
        'chart_div': chart_div
    }
    

def resumen_performance(request,player_id):
    context_performance_a = metrics_detail(request,player_id)
    context_performance_b = optimize_player_position(request,player_id)
    context_performance_c = player_performance_chart(request,player_id)
    context_performance_d = calculate_key_metrics(request, player_id)
    
    context = {**context_performance_a, **context_performance_b, **context_performance_c, **context_performance_d}
    
    return render(request, 'metrics/resumen_performance.html', context)