import tkinter as tk
import random

WIDTH, HEIGHT = 500, 500
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 10
BALL_SPEED = 15
PADDLE_SPEED = 40

# Colores
PADDLE_COLOR = "green"
BALL_COLOR = "red"

class PingPongGame:
    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.bind_all("<Key>", self.on_key_event)

        self.paddle_y = HEIGHT // 2
        self.ball_x = WIDTH // 2
        self.ball_y = HEIGHT // 2
        self.ball_dx = BALL_SPEED
        self.ball_dy = BALL_SPEED

        self.score = 0
        self.game_over = False
        self.update()

    def on_key_event(self, event):
        if event.keysym == "w" and self.paddle_y > 0:
            self.paddle_y -= PADDLE_SPEED
        elif event.keysym == "s" and self.paddle_y < HEIGHT - PADDLE_HEIGHT:
            self.paddle_y += PADDLE_SPEED

    def move_ball(self):
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_x <= 0 or self.ball_x >= WIDTH:
            self.ball_dx = -self.ball_dx

        if self.ball_y <= 0 or self.ball_y >= HEIGHT:
            self.ball_dy = -self.ball_dy

        if (
            self.ball_x <= PADDLE_WIDTH and
            self.paddle_y <= self.ball_y <= self.paddle_y + PADDLE_HEIGHT
        ):
            self.ball_dx = BALL_SPEED
            self.score += 1

        if self.ball_x <= 0:
            self.game_over = True

    def update(self):
        if not self.game_over:
            self.move_ball()
            self.canvas.delete(tk.ALL)

            # Dibujar la paleta
            self.canvas.create_rectangle(
                0, self.paddle_y,
                PADDLE_WIDTH, self.paddle_y + PADDLE_HEIGHT,
                fill=PADDLE_COLOR
            )

            # Dibujar la pelota
            self.canvas.create_oval(
                self.ball_x - BALL_SIZE, self.ball_y - BALL_SIZE,
                self.ball_x + BALL_SIZE, self.ball_y + BALL_SIZE,
                fill=BALL_COLOR
            )

            # Mostrar puntaje
            self.canvas.create_text(20, 20, text=f"Score: {self.score}", anchor=tk.NW)

            self.window.after(20, self.update)
        else:
            self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text=f"Game Over\nScore: {self.score}", anchor=tk.CENTER)

# Crear la ventana del juego
root = tk.Tk()
root.title("Ping Pong Game")
game = PingPongGame(root)

root.mainloop()
