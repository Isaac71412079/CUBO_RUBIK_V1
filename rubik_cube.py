from rubik_moves import RubikMoves
import copy

class RubikCube:
    def __init__(self):
        self.colors = ['W', 'G', 'O', 'R', 'B', 'Y']
        self.faces = {color: [[''] * 3 for _ in range(3)] for color in self.colors}

    def copy(self):
        new_cube = RubikCube()
        new_cube.faces = copy.deepcopy(self.faces)
        return new_cube

    def load_configuration(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) != 18:
                raise ValueError("Configuración invalida del cubo  vo numero incorrecto de lineas!!!")
            for i, line in enumerate(lines):
                if 1 <= i <= 3:
                    face_color = 'W'
                elif 4 <= i <= 6:
                    face_color = 'G'
                elif 7 <= i <= 9:
                    face_color = 'O'
                elif 10 <= i <= 12:
                    face_color = 'R'
                elif 13 <= i <= 15:
                    face_color = 'B'
                elif 16 <= i <= 18:
                    face_color = 'Y'
                if len(line.split()) != 3:
                    raise ValueError(f"Invalid configuration on line {i+1}: {line.strip()}")
                if i % 3 == 0:
                    face = [col.strip() for col in line.split()]
                elif i % 3 == 1:
                    face.extend([col.strip() for col in line.split()])
                else:
                    face.extend([col.strip() for col in line.split()])
                    if len(face) != 9:
                        raise ValueError(f"Invalid configuration on line {i+1}: {line.strip()}")
                    self.faces[face_color] = [face[:3], face[3:6], face[6:]]

    def is_valid_configuration(self):
        for color in self.colors:
            if sum(row.count(color) for face in self.faces.values() for row in face) != 9:
                return f"Error: Hay más o menos de 9 cuadraditos de color {color}"
        counts = {color: 0 for color in self.colors}
        for face in self.faces.values():
            counts[face[1][1]] += 1
        if any(count != 1 for count in counts.values()):
            return "Error: Hay más de un centro de un color"
        return True

    def print_cube(self):
        for row in range(3):
            for color in ['W', 'G', 'O', 'R', 'B', 'Y']:
                print(' '.join(self.faces[color][row]), end='   ')
            print()

    def print_cube_position(self):
        print("Posición de las caras del cubo:")
        print("'U'")
        self.print_face(self.faces['W'])
        print("'F'")
        self.print_face(self.faces['G'])
        print("'L'")
        self.print_face(self.faces['O'])
        print("'R'")
        self.print_face(self.faces['R'])
        print("'B'")
        self.print_face(self.faces['B'])
        print("'D'")
        self.print_face(self.faces['Y'])

    def print_face(self, face):
        for row in face:
            print(' '.join(row))
        print()

if __name__ == "__main__":
    cube = RubikCube()
    try:
        cube.load_configuration("configuracion_cubo3.txt")
        result = cube.is_valid_configuration()
        if result is True:
            print("Configuración del cubo válida:")
            cube.print_cube_position()
            print("Ingrese los movimientos (separados por espacios):")
            moves = input().strip().split()
            for move in moves:
                if hasattr(RubikMoves, move):
                    getattr(RubikMoves, move)(cube)
                else:
                    print(f"El movimiento '{move}' no es válido.")
            print("Después de los movimientos:")
            cube.print_cube_position()
        else:
            print(result)
    except ValueError as e:
        print("Error:", e)
