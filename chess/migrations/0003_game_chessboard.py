# Generated by Django 4.2.2 on 2023-12-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0002_remove_game_board_alter_game_turn'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='chessboard',
            field=models.JSONField(default=list),
        ),
    ]
