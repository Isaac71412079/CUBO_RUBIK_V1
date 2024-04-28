from rubik_cube import RubikCube
from rubik_moves import RubikMoves
import numpy as np
from datetime import datetime
import time

# Configuración inicial del cubo
xInitial = np.array([
    [[0, 0, 2], [1, 0, 2], [2, 0, 2]],
    [[0, 0, 1], [1, 0, 1], [2, 0, 1]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    [[0, 0, 2], [0, 1, 2], [0, 2, 2]],
    [[0, 0, 1], [0, 1, 1], [0, 2, 1]],
    [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    [[0, 1, 0], [1, 1, 0], [2, 1, 0]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],
    [[2, 0, 0], [2, 0, 1], [2, 0, 2]],
    [[2, 1, 0], [2, 1, 1], [2, 1, 2]],
    [[2, 2, 0], [2, 2, 1], [2, 2, 2]],
    [[2, 0, 2], [1, 0, 2], [0, 0, 2]],
    [[2, 1, 2], [1, 1, 2], [0, 1, 2]],
    [[2, 2, 2], [1, 2, 2], [0, 2, 2]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],
    [[0, 2, 1], [1, 2, 1], [2, 2, 1]],
    [[0, 2, 2], [1, 2, 2], [2, 2, 2]],
])

# Función para hacer un movimiento en el cubo
def make_move(cube, move):
    move_func = getattr(RubikMoves, move)
    move_func(cube)
    return cube

# Clase para representar el estado del cubo
class State:
    def __init__(self):
        self.cube = None
        self.g = 0
        self.h = 0
        self.parent = None
        self.move = None

# Implementación de IDA* para resolver el cubo de Rubik
class RubikIDAStar:
    def __init__(self):
        self.moves = ['U', 'U_prime', 'F', 'F_prime', 'L', 'L_prime', 'R', 'R_prime', 'B', 'B_prime', 'D', 'D_prime']
        self.target_cube = RubikCube()
        self.target_cube.load_configuration("cubo_configuracion3.txt")

    def manhattan_distance(self, cube):
        # Cálculo de la distancia Manhattan para la heurística
        corners = 0
        edges = 0
        for i in range(18):
            if i % 3 == 0 or i % 3 == 2:
                corners += self.manhattan_distance_helper(cube, i, 0, True) + self.manhattan_distance_helper(cube, i, 2, True)
                edges += self.manhattan_distance_helper(cube, i, 1, False)
            else:
                edges += self.manhattan_distance_helper(cube, i, 0, False) + self.manhattan_distance_helper(cube, i, 2, False)
        return max(corners / 12, edges / 8)

    def manhattan_distance_helper(self, cube, i, z, corner):
        # Función auxiliar para el cálculo de la distancia Manhattan
        c1 = xInitial[i, z]
        center = None
        for c in [1, 4, 7, 10, 13, 16]:
            if cube[i, z] == cube[c, 1]:
                center = c
                break

        if corner:
            c2 = xInitial[center - 1, 0]
            d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            c2 = xInitial[center - 1, 2]
            d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            c2 = xInitial[center + 1, 0]
            d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            c2 = xInitial[center + 1, 2]
            d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            return min(d1, d2, d3, d4)
        else:
            c2 = xInitial[center - 1, 1]
            d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            c2 = xInitial[center, 0]
            d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            c2 = xInitial[center, 2]
            d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            c2 = xInitial[center + 1, 1]
            d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
            return min(d1, d2, d3, d4)

    def ida_star_search(self, cube):
        def search(node, g, threshold):
            h = self.manhattan_distance(node)
            f = g + h
            if f > threshold:
                return f
            if np.array_equal(node, self.target_cube.configuration):
                return 'FOUND'
            min_value = float('inf')
            for move in self.moves:
                new_cube = make_move(np.array(node), move)
                if not np.array_equal(new_cube, node.parent) and not np.array_equal(new_cube, node.cube):
                    child = State()
                    child.cube = new_cube
                    child.parent = node.cube
                    child.move = move
                    child.g = g + 1
                    t = search(child, g + 1, threshold)
                    if t == 'FOUND':
                        return 'FOUND'
                    if t < min_value:
                        min_value = t
            return min_value

        start_state = State()
        start_state.cube = cube
        start_state.parent = None
        start_state.g = 0
        threshold = self.manhattan_distance(cube)
        while True:
            next_threshold = search(start_state, 0, threshold)
            if next_threshold == 'FOUND':
                return
            if next_threshold == float('inf'):
                return
            threshold = next_threshold

    def solve_cube(self):
        cube = np.array(xInitial)
        fmt = '%H:%M:%S'
        start_time = time.strftime(fmt)
        self.ida_star_search(cube)
        end_time = time.strftime(fmt)
        print("Time taken(sec):", datetime.strptime(end_time, fmt) - datetime.strptime(start_time, fmt))


# Ejemplo de uso
rubik_solver = RubikIDAStar()
rubik_solver.solve_cube()
