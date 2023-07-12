from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Move

def game_board(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    context = {
        'game': game,
    }
    return render(request, 'chess/board.html', context)

def make_move(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=game_id)
        move = Move(game=game, source=request.POST['source'], destination=request.POST['destination'])
        move.save()
        return redirect('game_board', game_id=game_id)
    
 