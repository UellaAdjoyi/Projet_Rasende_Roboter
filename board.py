import random

class Board:
    def __init__(self, grid_size=16):
        self.grid_size = grid_size
        self.grid = self.generate_grid()
        self.robots = {}
        self.target = None

    def generate_grid(self):
        # Création du plateau de 16x16 avec des plaques de 8x8 disposées aléatoirement
        grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        for i in range(4):
            start_x = (i % 2) * 8
            start_y = (i // 2) * 8
            for x in range(8):
                for y in range(8):
                    grid[start_y + y][start_x + x] = random.choice([0, 1])  # 0 = vide, 1 = mur
        return grid

    def place_robots(self, robots):
        positions = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size) if self.grid[y][x] == 0]
        random.shuffle(positions)
        for i, (name, robot) in enumerate(robots.items()):
            robot.pos = positions[i]

    def set_target(self, robot_color):
        # Place the target at the center and assign a robot color
        self.target = {"pos": (7, 7), "color": robot_color}
