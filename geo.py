
import tkinter as tk

# Tamaño del lienzo
WIDTH, HEIGHT = 900, 700

# Tamaño del cubo y velocidad de movimiento
CUBE_SIZE = 100
CUBE_SPEED = 50

# Color del cubo y del rastro
CUBE_COLOR = "black"
TRAIL_COLOR = "blue"

class CuboDrawer:
    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.bind_all("<Key>", self.on_key_event)

        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.trail = []

        self.update()

    def on_key_event(self, event):
        if event.keysym == "w":
            self.y -= CUBE_SPEED
        elif event.keysym == "a":
            self.x -= CUBE_SPEED
        elif event.keysym == "s":
            self.y += CUBE_SPEED
        elif event.keysym == "d":
            self.x += CUBE_SPEED

        self.trail.append((self.x, self.y))

    def update(self):
        self.canvas.delete(tk.ALL)

        # Dibuja el rastro
        for x, y in self.trail:
            self.canvas.create_rectangle(
                x - CUBE_SIZE, y - CUBE_SIZE, x + CUBE_SIZE, y + CUBE_SIZE,
                fill=TRAIL_COLOR
            )

        # Dibuja el cubo actual
        self.canvas.create_rectangle(
            self.x - CUBE_SIZE, self.y - CUBE_SIZE, self.x + CUBE_SIZE, self.y + CUBE_SIZE,
            fill=CUBE_COLOR
        )

        self.window.after(20, self.update)

root = tk.Tk()
root.title("Cubo Drawer")
game = CuboDrawer(root)

root.mainloop()
