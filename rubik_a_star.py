import heapq
from rubik_moves import RubikMoves
from rubik_cube import RubikCube
class RubikState:
    def __init__(self, cube, moves=[]):
        self.cube = cube
        self.moves = moves
        self.cost = len(self.moves) + self.heuristic()

    def heuristic(self):
        # Heurística más compleja (opcionalmente implementable)
        return sum(sum(1 for cell in row if cell != color) for face in self.cube.faces.values() for row in face for color in self.cube.colors)

    def __lt__(self, other):
        return self.cost < other.cost

def generate_moves(state):
    last_move = state.moves[-1] if state.moves else None
    moves = ['U', 'U_prime', 'L', 'L_prime', 'F', 'F_prime', 'R', 'R_prime', 'B', 'B_prime', 'D', 'D_prime']
    opposite = {'U': 'U_prime', 'U_prime': 'U', 'L': 'L_prime', 'L_prime': 'L', 'F': 'F_prime', 'F_prime': 'F',
                'R': 'R_prime', 'R_prime': 'R', 'B': 'B_prime', 'B_prime': 'B', 'D': 'D_prime', 'D_prime': 'D'}

    for move in moves:
        if last_move is None or (last_move != opposite[move]):
            new_cube = state.cube.copy()
            getattr(RubikMoves, move)(new_cube)
            new_state = RubikState(new_cube, state.moves + [move])
            yield new_state

def a_star_search(initial_cube):
    start_state = RubikState(initial_cube)
    frontier = []
    heapq.heappush(frontier, start_state)
    visited = set()

    while frontier:
        current_state = heapq.heappop(frontier)
        state_config = tuple(tuple(row) for face in current_state.cube.faces.values() for row in face)

        if current_state.heuristic() == 0:
            return current_state.moves

        if state_config not in visited:
            visited.add(state_config)
            for next_state in generate_moves(current_state):
                heapq.heappush(frontier, next_state)

    return None

# Ejecución del solucionador
if __name__ == "__main__":
    cube = RubikCube()
    cube.load_configuration("configuracion_cubo3.txt")
    solution_moves = a_star_search(cube)
    print("No. Pasos:", len(solution_moves))
    print("Pasos:", ' '.join(solution_moves))