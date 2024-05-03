from collections import deque
from rubik_cube import RubikCube, RubikMoves

class Node:
    def __init__(self, cube, move=None, parent=None):
        self.cube = cube
        self.move = move
        self.parent = parent

def is_solved(cube):
    target = [['W']*3, ['G']*3, ['O']*3, ['R']*3, ['B']*3, ['Y']*3]
    for face in target:
        if cube.faces[face[0][0]] != [face for _ in range(3)]:
            return False
    return True

def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    return path[::-1]

def bfs_solve(start_cube):
    initial_node = Node(start_cube)
    queue = deque([initial_node])
    visited = set()
    visited.add(str(start_cube.faces))

    while queue:
        current_node = queue.popleft()
        current_cube = current_node.cube

        if is_solved(current_cube):
            return reconstruct_path(current_node)
        
        for move_name in RubikMoves.get_all_moves():
            new_cube = current_cube.copy()
            move = getattr(RubikMoves, move_name)
            move(new_cube)
            cube_state_str = str(new_cube.faces)
            if cube_state_str not in visited:
                visited.add(cube_state_str)
                queue.append(Node(new_cube, move=move_name, parent=current_node))
    return []

if __name__ == "__main__":
    cube = RubikCube()
    cube.load_configuration("configuracion_cubo3.txt")
    if cube.is_valid_configuration():
        solution = bfs_solve(cube)
        print(f"No. Pasos: {len(solution)}")
        print("Pasos:", ' '.join(solution))
    else:
        print("Configuración inicial no válida.")
