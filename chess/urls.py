from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    path('', views.game_board, {'game_id': 123}, name='default_game_board'),
    path('game/<int:game_id>/', views.game_board, name='game_board'),
    path('game/<int:game_id>/move/', views.make_move, name='make_move'),
]