# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Move

def game_board(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    # Assuming that your Game model has a chessboard attribute
    chessboard = game.chessboard  # Adjust this line based on your actual model

    context = {
        'game': game,
        'chessboard': chessboard,  # Pass the chessboard to the template
    }
    return render(request, 'chess/board.html', context)

def make_move(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        source = request.POST['source']
        destination = request.POST['destination']

        # Validate the move based on chess rules
        if is_valid_move(game, source, destination):
            # Make the move
            move_piece(game, source, destination)

            # Update game state
            game.turn = 'white' if game.turn == 'black' else 'black'
            game.save()

            return redirect('chess:game_board', game_id=game_id)
        else:
            error_message = "Invalid move. Please try again."
            context = {
                'game': game,
                'error_message': error_message,
            }
            return render(request, 'chess/board.html', context)

    # Handle GET request (if needed)
    return redirect('chess:game_board', game_id=game_id)

def is_valid_move(game, source, destination):
    """
    Validate the move based on chess rules.
    This is a placeholder function; you need to implement your own logic.
    """
    # Implement logic for validating moves based on the rules of chess
    # Check if the move is valid for the specific piece
    # Check if the move puts the own king in check, etc.
    return True  # Placeholder

def move_piece(game, source, destination):
    """
    Move the chess piece on the board.
    Implement specific logic for each piece type.
    """
    # Placeholder logic; you need to implement your own piece movement rules
    # This might involve checking the piece type, validating the move, updating the board, etc.
    piece = game.get_piece_at(int(source[0]), int(source[1]))
    game.chessboard[int(source[0])][int(source[1])] = None
    game.chessboard[int(destination[0])][int(destination[1])] = piece

    # Save the move to the database
    move = Move(game=game, source=source, destination=destination)
    move.save()
