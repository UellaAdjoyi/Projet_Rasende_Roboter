from ai import a_star

class Robot:
    def __init__(self, color):
        self.color = color
        self.pos = (0,0)

    def move(self, grid, robots_positions, target_pos):
        """Déplace le robot vers la cible en utilisant l'algorithme A*"""
        path = a_star(self.pos, target_pos, grid, robots_positions)
        if path:
            # Si un chemin est trouvé, le robot suit ce chemin
            self.pos = path[0]  # Le premier mouvement à faire
            return True
        return False

    def is_at_target(self, target_pos):
        return self.pos == target_pos
