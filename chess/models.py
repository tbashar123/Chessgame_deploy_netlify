# models.py
from django.db import models

class Game(models.Model):
    # Add your existing Game model fields here

    # Assuming that the chessboard is a list of lists representing the board
    chessboard = models.JSONField(default=list)  
    turn = models.CharField(max_length=5)  # Adjust the max_length as needed

    def get_piece_at(self, row, col):
        return self.chessboard[row][col] if 0 <= row < 8 and 0 <= col < 8 else None

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    source = models.CharField(max_length=2)
    destination = models.CharField(max_length=2)
    # Add other fields as needed
