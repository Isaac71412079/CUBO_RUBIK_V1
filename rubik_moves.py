#   U - Giro de la cara superior en sentido horario.
#   U_prime - Giro de la cara superior en sentido anti-horario.
#   F - Giro de la cara frontal en sentido horario.
#   F_prime - Giro de la cara frontal en sentido anti-horario.
#   L - Giro de la cara izquierda en sentido horario.
#   L_prime - Giro de la cara izquierda en sentido anti-horario.
#   R - Giro de la cara derecha en sentido horario.
#   R_prime - Giro de la cara derecha en sentido anti-horario.
#   B - Giro de la cara trasera en sentido horario.
#   B_prime - Giro de la cara trasera en sentido anti-horario.
#   D - Giro de la cara inferior en sentido horario.
#   D_prime - Giro de la cara inferior en sentido anti-horario.

#SE HIZO CORRECION PARA LOS MOVIMIENTOS U y U', F y F', L y L', R y R', B y B'.

class RubikMoves:
    @staticmethod
    def rotate_face_clockwise(face):
        """
        Rotate a face clockwise.
        """
        face[0][0], face[0][2], face[2][2], face[2][0] = face[2][0], face[0][0], face[0][2], face[2][2]
        face[0][1], face[1][2], face[2][1], face[1][0] = face[1][0], face[0][1], face[1][2], face[2][1]

    @staticmethod
    def rotate_face_counterclockwise(face):
        """
        Rotate a face counterclockwise.
        """
        face[0][0], face[0][2], face[2][2], face[2][0] = face[0][2], face[2][2], face[2][0], face[0][0]
        face[0][1], face[1][2], face[2][1], face[1][0] = face[1][2], face[2][1], face[1][0], face[0][1]

    @staticmethod
    def U(cube): #MOVIMIENTO CORRECTO
        """
        Rotate the upper face clockwise.
        """
        # Rotate face
        RubikMoves.rotate_face_clockwise(cube.faces['W'])
        # Rotate adjacent stickers
        top_row = cube.faces['G'][0]
        cube.faces['G'][0] = cube.faces['R'][0]
        cube.faces['R'][0] = cube.faces['B'][0]
        cube.faces['B'][0] = cube.faces['O'][0]
        cube.faces['O'][0] = top_row

    @staticmethod
    def U_prime(cube): #MOVIMIENTO CORRECTO
        """
        Rotate the upper face counterclockwise.
        """
        # Rotate face
        RubikMoves.rotate_face_counterclockwise(cube.faces['W'])
        # Rotate adjacent stickers
        top_row = cube.faces['G'][0]
        cube.faces['G'][0] = cube.faces['O'][0]
        cube.faces['O'][0] = cube.faces['B'][0]
        cube.faces['B'][0] = cube.faces['R'][0]
        cube.faces['R'][0] = top_row

    @staticmethod
    def F(cube): #MOVIMIENTO CORRECTO
        """
        Rotate the front face clockwise.
        """
        # Rotate face
        RubikMoves.rotate_face_clockwise(cube.faces['G'])
        # Rotate adjacent stickers
        top_row = cube.faces['W'][2].copy()
        cube.faces['W'][2] = [cube.faces['O'][2-i][2] for i in range(3)]
        for i in range(3):
            cube.faces['O'][i][2] = cube.faces['Y'][0][i]  # Se actualiza la fila inferior de 'O' con la fila superior de 'Y'
        for i in range(3):
            cube.faces['Y'][0][i] = cube.faces['R'][2 - i][0]  # Se actualiza la fila superior de 'Y' con la columna izquierda de 'R'
        for i in range(3):
            cube.faces['R'][i][0] = top_row[i]  # Se actualiza la columna izquierda de 'R' con la fila superior de 'W'

    @staticmethod
    def F_prime(cube): #MOVIMIENTO CORRECTO
        """
        Rotate the front face counterclockwise.
        """
        # Rotate face
        RubikMoves.rotate_face_counterclockwise(cube.faces['G'])
        # Rotate adjacent stickers
        top_row = cube.faces['W'][2].copy()
        cube.faces['W'][2] = [cube.faces['R'][i-2][0] for i in range(3)][::-1]
        for i in range(3):
            cube.faces['R'][i][0] = cube.faces['Y'][0][2 - i]  # Se actualiza la columna izquierda de 'R' con la fila superior invertida de 'Y'
        for i in range(3):
            cube.faces['Y'][0][i] = cube.faces['O'][1-i][2]  # Se actualiza la fila superior de 'Y' con la fila inferior de 'O'
        for i in range(3):
            cube.faces['O'][i][2] = top_row[2-i]  # Se actualiza la fila inferior de 'O' con la fila superior de 'W'

#SE HIZO CORRECION PARA LOS MOVIMIENTOS U y U', F y F'.

    @staticmethod
    def L(cube): #MOVIMIENTO INCORRECTO
        """
        Rotate the left face clockwise.
        """
        RubikMoves.rotate_face_clockwise(cube.faces['O'])
        left_column = [cube.faces['W'][i][0] for i in range(3)]
        for i in range(3):
            cube.faces['W'][i][0] = cube.faces['B'][2 - i][2]
        for i in range(3):
            cube.faces['B'][i][2] = cube.faces['Y'][i][0]
        for i in range(3):
            cube.faces['Y'][i][0] = cube.faces['G'][i][0]
        for i in range(3):
            cube.faces['G'][i][0] = left_column[i]

    @staticmethod
    def L_prime(cube): #MOVIMIENTO CORRECTO
        """
        Rotate the left face counterclockwise.
        """
        RubikMoves.rotate_face_counterclockwise(cube.faces['O'])
        left_column = [cube.faces['W'][i][0] for i in range(3)]
        for i in range(3):
            cube.faces['W'][i][0] = cube.faces['G'][i][0]
        for i in range(3):
            cube.faces['G'][i][0] = cube.faces['Y'][i][0]
        for i in range(3):
            cube.faces['Y'][i][0] = cube.faces['B'][2-i][2]
        for i in range(3):
            cube.faces['B'][i][2] = left_column[2-i]

#SE HIZO CORRECION PARA LOS MOVIMIENTOS U y U', F y F', L y L'.

    @staticmethod
    def R(cube): #MOVIMIENTO CORRECTO
        """
        Rotate the right face clockwise.
        """
        RubikMoves.rotate_face_clockwise(cube.faces['R'])
        right_column = [cube.faces['W'][i][2] for i in range(3)]
        for i in range(3):
            cube.faces['W'][i][2] = cube.faces['G'][i][2]
        for i in range(3):
            cube.faces['G'][i][2] = cube.faces['Y'][i][2]
        for i in range(3):
            cube.faces['Y'][i][2] = cube.faces['B'][2-i][0]
        for i in range(3):
            cube.faces['B'][i][0] = right_column[2 - i]

    @staticmethod
    def R_prime(cube): #MOVIMIENTO CORRECTO
        """
        Rotate the right face counterclockwise.
        """
        RubikMoves.rotate_face_counterclockwise(cube.faces['R'])
        right_column = [cube.faces['W'][i][2] for i in range(3)]
        for i in range(3):
            cube.faces['W'][i][2] = cube.faces['B'][2-i][0]
        for i in range(3):
            cube.faces['B'][i][0] = cube.faces['Y'][2 - i][2]
        for i in range(3):
            cube.faces['Y'][i][2] = cube.faces['G'][i][2]
        for i in range(3):
            cube.faces['G'][i][2] = right_column[i]

#SE HIZO CORRECION PARA LOS MOVIMIENTOS U y U', F y F', L y L', R y R'.

    @staticmethod
    def B(cube): 
        """
        Rotate the back face clockwise.
        """
        RubikMoves.rotate_face_clockwise(cube.faces['B'])
        top_row_B = cube.faces['W'][0].copy()

        cube.faces['W'][0] = [cube.faces['R'][i][2] for i in range(3)][::-1]
        cube.faces['R'][2][2], cube.faces['R'][1][2], cube.faces['R'][0][2] = cube.faces['Y'][2]
        cube.faces['Y'][2] = [cube.faces['O'][i][0] for i in range(3)]
        for i in range(3):
            cube.faces['O'][i][0] = top_row_B[2-i]

    @staticmethod
    def B_prime(cube): 
        """
        Rotate the back face counterclockwise.
        """
        RubikMoves.rotate_face_counterclockwise(cube.faces['B'])
        top_row_B = cube.faces['W'][0].copy()
        cube.faces['W'][0] = [cube.faces['O'][i][0] for i in range(3)]
        cube.faces['O'][0][0], cube.faces['O'][1][0], cube.faces['O'][2][0] = cube.faces['Y'][2]
        cube.faces['Y'][2] = [cube.faces['R'][i][2] for i in range(3)][::-1]
        for i in range(3):
            cube.faces['R'][i][2] = top_row_B[i]

#SE HIZO CORRECION PARA LOS MOVIMIENTOS U y U', F y F', L y L', R y R', B y B'.

    @staticmethod
    def D(cube):
        """
        Rotate the down face clockwise.
        """
        RubikMoves.rotate_face_clockwise(cube.faces['Y'])
        bottom_row = cube.faces['B'][2]
        cube.faces['B'][2] = cube.faces['R'][2]
        cube.faces['R'][2] = cube.faces['G'][2]
        cube.faces['G'][2] = cube.faces['O'][2]
        cube.faces['O'][2] = bottom_row

    @staticmethod
    def D_prime(cube):
        """
        Rotate the down face counterclockwise.
        """
        RubikMoves.rotate_face_counterclockwise(cube.faces['Y'])
        bottom_row = cube.faces['B'][2]
        cube.faces['B'][2] = cube.faces['O'][2]
        cube.faces['O'][2] = cube.faces['G'][2]
        cube.faces['G'][2] = cube.faces['R'][2]
        cube.faces['R'][2] = bottom_row


#SE HIZO CORRECION PARA TODOS LOS MOVIMIENTOS U y U', F y F', L y L', R y R', B y B', D y D'.
