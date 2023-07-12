from django.db import models

class Game(models.Model):
    # Define your fields to represent the game state (e.g., chessboard, player turn, etc.)
    board = models.TextField()
    turn = models.CharField(max_length=1)
    # Add more fields as needed

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # Define your fields to represent a move (e.g., source, destination, etc.)
    source = models.CharField(max_length=2)
    destination = models.CharField(max_length=2)
    # Add more fields as needed
