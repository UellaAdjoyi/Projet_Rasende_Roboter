class Target:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.pos[0] * 40 + 20, self.pos[1] * 40 + 20), 15)
