import tkinter as tk
from tkinter import messagebox
from StackHanoi import Stack

class HanoiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanoi")
        self.num_disks = 0
        self.num_optimal_moves = 0
        self.move_count = 0
        self.selected_stack = None

        self.stacks = [
            Stack("Izquierda"),
            Stack("Media"),
            Stack("Derecha")
        ]

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="lightgray")
        self.canvas.pack()

        self.info_label = tk.Label(self.root, text="Bienvenido a las Torres de Hanoi", font=("Arial", 14))
        self.info_label.pack()

        self.move_count_label = tk.Label(self.root, text="Movimientos: 0", font=("Arial", 12))
        self.move_count_label.pack()

        self.optimal_moves_label = tk.Label(self.root, text="Número óptimo de movimientos: 0", font=("Arial", 12))
        self.optimal_moves_label.pack()

        self.warning_label = tk.Label(self.root, text="", fg="red", font=("Arial", 12))
        self.warning_label.pack()

        self.disk_input_label = tk.Label(self.root, text="Número de discos (máximo 8):", font=("Arial", 12))
        self.disk_input_label.pack()

        self.disk_input = tk.Entry(self.root)
        self.disk_input.pack()

        self.start_button = tk.Button(self.root, text="Iniciar Juego", command=self.start_game)
        self.start_button.pack()

        self.reset_button = tk.Button(self.root, text="Reiniciar", command=self.reset_game)
        self.reset_button.pack()

        self.left_button = tk.Button(self.root, text="Pila Izquierda", command=lambda: self.select_stack(0))
        self.left_button.pack(side="left", padx=10)

        self.middle_button = tk.Button(self.root, text="Pila Media", command=lambda: self.select_stack(1))
        self.middle_button.pack(side="left", padx=10)

        self.right_button = tk.Button(self.root, text="Pila Derecha", command=lambda: self.select_stack(2))
        self.right_button.pack(side="left", padx=10)

    def start_game(self):
        try:
            self.num_disks = int(self.disk_input.get())
            if (self.num_disks < 3) or (self.num_disks > 8):
                raise ValueError
        except ValueError:
            self.warning_label.config(text="Por favor, ingresa un número válido de discos (máximo 8).")
            return

        self.num_optimal_moves = (2 ** self.num_disks) - 1
        self.optimal_moves_label.config(text=f"Número óptimo de movimientos: {self.num_optimal_moves}")
        self.reset_game()
        self.info_label.config(text=f"Juego iniciado con {self.num_disks} discos.")
        self.warning_label.config(text="")

        self.stacks[0].top_item = None
        for disk in range(self.num_disks, 0, -1):
            self.stacks[0].push(disk)

        self.move_count = 0
        self.update_move_count()
        self.render_game()

    def get_stack_items(self, stack_index):
        stack = self.stacks[stack_index]
        items = []
        pointer = stack.top_item
        while (pointer):
            items.append(pointer.get_value())
            pointer = pointer.get_next_node()
        items.reverse()
        return items

    def render_game(self):
        self.canvas.delete("all")

        self.render_stack(0, 150)
        self.render_stack(1, 300)
        self.render_stack(2, 450)

    def render_stack(self, stack_index, x_position):
        stack_items = self.get_stack_items(stack_index)
        y_position = 300
        for i, disk in enumerate(stack_items):
            self.canvas.create_rectangle(x_position - disk * 15, y_position - i * 25, 
                                          x_position + disk * 15, y_position - (i + 1) * 25, fill="green")
            self.canvas.create_text(x_position, y_position - i * 25 - 12, text=str(disk), fill="white")

    def update_move_count(self):
        self.move_count_label.config(text=f"Movimientos: {self.move_count}")

    def select_stack(self, stack_index):
        if (self.selected_stack is None):
            self.selected_stack = stack_index
            self.warning_label.config(text=f"Seleccionaste la pila {['Izquierda', 'Media', 'Derecha'][stack_index]}. Ahora selecciona una pila destino.", fg="blue")
        else:
            from_stack = self.stacks[self.selected_stack]
            to_stack = self.stacks[stack_index]

            if (self.is_valid_move(from_stack, to_stack)):
                disk = from_stack.pop()
                to_stack.push(disk)
                self.move_count += 1
                self.update_move_count()
                self.check_win()
            else:
                self.warning_label.config(text="Movimiento no válido.", fg="red")

            self.selected_stack = None
        self.render_game()

    def is_valid_move(self, from_stack, to_stack):
        if (from_stack.get_size() == 0):
            return False
        if (to_stack.get_size() > 0) and (from_stack.peek() > to_stack.peek()):
            return False
        return True

    def check_win(self):
        if (self.stacks[2].get_size() == self.num_disks):
            self.render_game()  # Asegurarse de que la visualización esté actualizada
            messagebox.showinfo("¡Felicidades!", f"¡Completaste el juego en {self.move_count} movimientos!")
            self.reset_game()


    def reset_game(self):
        self.stacks[0].top_item = None
        self.stacks[1].top_item = None
        self.stacks[2].top_item = None
        self.selected_stack = None
        self.warning_label.config(text="")
        self.render_game()


root = tk.Tk()
game = HanoiGame(root)
root.mainloop()
