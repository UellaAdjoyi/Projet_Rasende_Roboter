# game.py
import random
from ai import astar

# Initialisation des robots
robots = {
    "red": {"color": (255, 0, 0), "pos": (1, 1)},
    "green": {"color": (0, 255, 0), "pos": (3, 3)},
    "blue": {"color": (0, 0, 255), "pos": (5, 5)},
    "yellow": {"color": (255, 255, 0), "pos": (7, 7)},
}

target = {"pos": (8, 8), "color": "red"}

def move_robot_with_ai(robot_color, target_pos, grid):
    """Déplace un robot en utilisant l'algorithme A*"""
    start = robots[robot_color]["pos"]
    path = astar(start, target_pos, grid, robots)
    
    if path:
        next_pos = path[1]  # Prendre la deuxième position du chemin (car la première est la position actuelle)
        robots[robot_color]["pos"] = next_pos

def update_game(grid):
    """Mise à jour du jeu, faire déplacer l'IA"""
    move_robot_with_ai(target["color"], target["pos"], grid)
