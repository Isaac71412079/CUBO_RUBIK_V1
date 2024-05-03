from tkinter import Tk, Label, Button, Canvas, StringVar, Entry, Frame, Menu
from rubik_cube import RubikCube, RubikMoves
import rubik_ida_star
import rubik_a_star
import rubik_bfs

class RubikCubeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Rubik Cube Solver')

        self.title_label = Label(master, text="Rubik Cube Solver", font=("Times New Roman", 20, "bold"))
        self.title_label.pack(pady=10)  # Añade un poco de espacio verticalmente para que no esté tan pegado al canvas

        # Configuración de Canvas para visualizar el cubo
        self.canvas = Canvas(master, width=550, height=400)
        self.canvas.pack()

        self.status_var = StringVar()
        self.status_label = Label(master, textvariable=self.status_var, wraplength=450)
        self.status_label.pack()

        self.entry_var = StringVar()
        self.entry = Entry(master, textvariable=self.entry_var, width=50)
        self.entry.pack()

        self.enter_button = Button(master, text="MOVE", command=self.enter_moves, bg='blue', fg='white', activebackground='lightblue')
        self.enter_button.pack()

        self.solve_button = Button(master, text="IDA STAR SOLVE", command=self.solve_cube_ida_star)
        self.solve_button.pack()

        self.solve_button = Button(master, text="A STAR SOLVE", command=self.solve_cube_a_star)
        self.solve_button.pack()

        self.solve_button = Button(master, text="BFS SOLVE", command=self.solve_cube_bfs)
        self.solve_button.pack()

        self.enter_button = Button(master, text="RESET FROM FILE", command=self.reset_cube, bg='purple', fg='white', activebackground='pink')
        self.enter_button.pack()

        self.enter_button = Button(master, text="RESET IN ORDER", command=self.reset_cube_to_original, bg='green', fg='black', activebackground='yellow')
        self.enter_button.pack()

        self.cube = RubikCube()
        self.reset_cube()

    def enter_moves(self):
        moves = self.entry_var.get().strip().split()
        for move in moves:
            if hasattr(RubikMoves, move):
                getattr(RubikMoves, move)(self.cube)
            else:
                self.status_var.set(f"El movimiento '{move}' no es válido.")
                return
        self.update_canvas()

    def solve_cube_ida_star(self):
        # Asume que rubik_ida_star.ida_star ya está correctamente implementado
        solution = rubik_ida_star.ida_star(self.cube)
        if solution:
            state, solution_path = solution
            self.status_var.set(f"Solución IDA*: {' '.join(solution_path)} en {len(solution_path)} pasos.")
        else:
            self.status_var.set("No se encontró solución.")
        self.update_canvas()

    def solve_cube_a_star(self):
        # Asume que rubik_ida_star.ida_star ya está correctamente implementado
        solution = rubik_a_star.a_star_search(self.cube)
        if solution:
            state, solution_path = solution
            self.status_var.set(f"Solución A*: {' '.join(solution_path)} en {len(solution_path)} pasos.")
        else:
            self.status_var.set("No se encontró solución.")
        self.update_canvas()

    def solve_cube_bfs(self):
        # Asume que rubik_ida_star.ida_star ya está correctamente implementado
        solution = rubik_bfs.bfs_solve(self.cube)
        if solution:
            state, solution_path = solution
            self.status_var.set(f"Solución A*: {' '.join(solution_path)} en {len(solution_path)} pasos.")
        else:
            self.status_var.set("No se encontró solución.")
        self.update_canvas()

    def reset_cube(self):
        self.cube = RubikCube()
        self.cube.load_configuration("configuracion_cubo3.txt")
        self.entry_var.set('')
        self.update_canvas()
        self.status_var.set("Cubo cargado y reseteado.")

    def reset_cube_to_original(self):
        self.cube = RubikCube()
        self.cube.load_configuration("configuracion_cubo.txt")
        self.entry_var.set('')
        self.update_canvas()
        self.status_var.set("Cubo cargado en Orden")

    def update_canvas(self):
        self.canvas.delete("all")
        self.draw_cube()

    def draw_cube(self):
        colors = {'W': 'white', 'G': 'green', 'O': 'orange', 'R': 'red', 'B': 'blue', 'Y': 'yellow'}
        size = 40
        # Draw the unfolded cube: U, L, F, R, B, D
        faces = ['W', 'O', 'G', 'R', 'B', 'Y']
        positions = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)]  # x, y positions on canvas

        for face, pos in zip(faces, positions):
            for i in range(3):
                for j in range(3):
                    x0 = (pos[0] * 3 + j) * size
                    y0 = (pos[1] * 3 + i) * size
                    x1 = x0 + size
                    y1 = y0 + size
                    color = colors[self.cube.faces[face][i][j]]
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black')

def main():
    root = Tk()
    app = RubikCubeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
