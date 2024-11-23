import pygame
import random
from robot import Robot
from board import Board
from target import Target

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rasende Roboter")

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Variables de jeu
robots = {'red': Robot('red'), 'green': Robot('green'), 'blue': Robot('blue'), 'yellow': Robot('yellow')}
board = Board()
board.place_robots(robots)
target = Target((7, 7), 'red')
ai_difficulty = 1  # 1 = facile, 2 = difficile
score = 0

# Fonction pour afficher le texte à l'écran
def display_text(text, color, x, y):
    font = pygame.font.SysFont('Arial', 24)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Fonction principale de jeu
def main():
    global ai_difficulty, score
    running = True
    clock = pygame.time.Clock()

    # Choisir la difficulté de l'IA
    while running:
        screen.fill(WHITE)
        display_text("Choisissez la difficulté de l'IA:", RED, 50, 50)
        display_text("1 - Facile", BLUE, 50, 100)
        display_text("2 - Difficile", BLUE, 50, 150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= pygame.mouse.get_pos()[1] <= 120:
                    ai_difficulty = 1
                    running = False
                elif 50 <= pygame.mouse.get_pos()[1] <= 170:
                    ai_difficulty = 2
                    running = False

        pygame.display.flip()
        clock.tick(30)

    # Boucle de jeu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Déplacer l'IA
        if ai_difficulty == 1:
            robots['red'].move(board.grid, [robot.pos for robot in robots.values()], target.pos)
        elif ai_difficulty == 2:
            robots['red'].move(board.grid, [robot.pos for robot in robots.values()], target.pos)

        # Vérifier si l'IA a atteint la cible
        if robots['red'].is_at_target(target.pos):
            score += 1
            print(f"Score: {score} - IA a atteint la cible!")

        # Affichage
        screen.fill(WHITE)
        for robot in robots.values():
            pygame.draw.circle(screen, RED if robot.color == 'red' else BLUE if robot.color == 'blue' else YELLOW if robot.color == 'yellow' else GREEN,
                   robot.pos[0] * 40 + 20, robot.pos[1] * 40 + 20, 15)


        target.draw(screen)

        # Afficher le score
        display_text(f"Score: {score}", GREEN, 500, 50)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
