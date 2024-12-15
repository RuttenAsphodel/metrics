from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('player_list', views.player_list, name='player_list'),
    path('<int:player_id>/player_detail', views.player_detail, name='player_detail'),
    path('create/', views.player_create, name='player_create'),
    path('<int:player_id>/update_player/', views.player_update, name='player_update'),
    path('<int:player_id>/delete/', views.player_delete, name='player_delete'),
    path('<int:player_id>/', views.metrics_detail, name='metrics_detail'),
    path('<int:player_id>/create/', views.metrics_create, name='metrics_create'),
    path('<int:player_id>/update_metrics/', views.metrics_update, name='metrics_update'),
    path('<int:player_id>/delete/', views.metrics_delete, name='metrics_delete'),
    path('<int:player_id>/key_metrics/', views.calculate_key_metrics, name='calculate_key_metrics'),
    path('<int:player_id>/optimize_position/', views.optimize_player_position, name='optimize_position'),
    path('<int:player_id>/performance_charts/', views.player_performance_chart, name='performance_charts'),
    path('<int:player_id>/resumen_performance/', views.resumen_performance, name='resumen_performance'),
]