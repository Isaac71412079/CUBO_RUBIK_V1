from rubik_cube import RubikCube, RubikMoves
#Solucion a configuracion_cubo3.txt: L B L F U U D_prime R R B_prime L F R D R R F F D_prime F F U_prime R R L L U U
class State:
    def __init__(self, cube, g=0, h=0, parent=None, move=None):
        self.cube = cube
        self.g = g
        self.h = h
        self.parent = parent
        self.move = move

def heuristic(cube):
    # Esta es una heurística muy simplificada: contar el número de piezas fuera de lugar
    misplaced = 0
    for color, face in cube.faces.items():
        for row in face:
            for cell in row:
                if cell != color:
                    misplaced += 1
    return misplaced

def goal_reached(state):
    # Revisar que cada cara del cubo tenga un color uniforme
    return all(cell == color for color, face in state.cube.faces.items() for row in face for cell in row)

def ida_star(start_cube):
    start = State(cube=start_cube, h=heuristic(start_cube))
    threshold = start.h
    path = []
    while True:
        temp, new_threshold = search(start, 0, threshold, path, float('inf'))
        if isinstance(temp, tuple):  
            return temp
        if new_threshold == float('inf'):  
            break
        threshold = new_threshold  
    return None

def apply_move(cube, move):
    getattr(RubikMoves, move)(cube)

def undo_move(cube, move):
    reverse_move = move + "_prime" if not move.endswith("_prime") else move[:-6]
    getattr(RubikMoves, reverse_move)(cube)

def search(current_state, g, threshold, path, minimum):
    f = g + current_state.h
    if f > threshold:
        return None, min(minimum, f)
    if goal_reached(current_state):
        return (current_state, path), minimum

    for move in RubikMoves.get_all_moves():
        apply_move(current_state.cube, move)
        new_state = State(current_state.cube, g + 1, heuristic(current_state.cube), current_state, move)
        
        if move not in path:
            path.append(move)
            temp, new_minimum = search(new_state, g + 1, threshold, path, minimum)
            if isinstance(temp, tuple):
                return temp, minimum
            minimum = new_minimum
            path.pop()

        undo_move(current_state.cube, move)

    return None, minimum

if __name__ == "__main__":
    cube = RubikCube()
    cube.load_configuration("configuracion_cubo3.txt")
    if isinstance(cube.is_valid_configuration(), bool) and cube.is_valid_configuration():
        result = ida_star(cube)
        if result:
            state, solution_path = result
            print(f"No. Pasos: {len(solution_path)}")
            print("Pasos:", ' '.join(solution_path))
        else:
            print("No se encontró solución dentro de los límites de profundidad dados")
    else:
        print("Configuración no válida")
