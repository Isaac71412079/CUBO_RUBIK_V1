import heapq
from rubik_cube import RubikCube
from rubik_moves import RubikMoves

class Node:
    def __init__(self, cube, g=0, h=0, parent=None, move=None):
        self.cube = cube
        self.g = g  # Costo desde el inicio
        self.h = h  # Heurística al objetivo
        self.f = g + h  # Costo total estimado
        self.parent = parent  # Nodo padre
        self.move = move  # Movimiento que llevó a este estado

    def __lt__(self, other):
        return self.f < other.f  # Necesario para la cola de prioridad

def heuristic(cube):
    # Esta es una heurística simplificada que cuenta el número de piezas fuera de lugar
    goal = ['W', 'G', 'O', 'R', 'B', 'Y']
    mismatch = 0
    for color in goal:
        goal_state = [[color]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if cube.faces[color][i][j] != goal_state[i][j]:
                    mismatch += 1
    return mismatch

def a_star_solve(cube):
    initial_node = Node(cube.copy(), h=heuristic(cube))
    open_set = []
    heapq.heappush(open_set, initial_node)
    visited = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.h == 0:  # Chequear si es el estado objetivo
            return reconstruct_path(current_node)

        visited.add(current_node.cube)

        for move in [RubikMoves.U, RubikMoves.U_prime, RubikMoves.F, RubikMoves.F_prime, RubikMoves.L, RubikMoves.L_prime, RubikMoves.R, RubikMoves.R_prime, RubikMoves.B, RubikMoves.B_prime, RubikMoves.D, RubikMoves.D_prime]:
            new_cube = current_node.cube.copy()
            move(new_cube)
            if new_cube in visited:
                continue
            new_node = Node(new_cube, current_node.g + 1, heuristic(new_cube), current_node, move.__name__)
            heapq.heappush(open_set, new_node)

def reconstruct_path(node):
    path = []
    while node:
        if node.move:
            path.append(node.move)
        node = node.parent
    return path[::-1]  # Invertir para mostrar los pasos desde el inicio al final

if __name__ == "__main__":
    cube = RubikCube()
    cube.load_configuration("configuracion_cubo1.txt")
    solution_path = a_star_solve(cube)
    print("Pasos para resolver el cubo:", solution_path)