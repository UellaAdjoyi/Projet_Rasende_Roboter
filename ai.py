import heapq

def a_star(start, goal, grid, robots_positions):
    """Algorithme A* pour trouver le chemin optimal d'un robot vers la cible"""
    open_list = []
    closed_list = set()
    came_from = {}

    # Fonction de distance de Manhattan (plus simple pour ce type de grille)
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    # Coûts
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, goal)}

    # Ajouter le point de départ à la liste ouverte
    heapq.heappush(open_list, (f_score[start], start))

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruire le chemin à partir des points parents
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        closed_list.add(current)

        # Déplacer dans les directions possibles (haut, bas, gauche, droite)
        neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        for neighbor in neighbors:
            x, y = neighbor
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[y][x] == 1 or neighbor in robots_positions:
                continue  # Ignorer les murs ou robots déjà présents

            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return []  # Aucun chemin trouvé
