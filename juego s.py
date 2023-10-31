import tkinter as tk
import random

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 10
SNAKE_SPEED = 60

# Direcciones
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

# Colores
SNAKE_COLOR = "green"
FOOD_COLOR = "blue"

class SnakeGame:
    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.bind_all("<Key>", self.on_key_event)
        
        self.reset_game()

    def reset_game(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.direction = RIGHT
        self.score = 0
        self.game_over = False
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            if (x, y) not in self.snake:
                return x, y

    def on_key_event(self, event):
        if (event.keysym == "Up" or event.keysym == "w") and self.direction != DOWN:
            self.direction = UP
        elif (event.keysym == "Down" or event.keysym == "s") and self.direction != UP:
            self.direction = DOWN
        elif (event.keysym == "Left" or event.keysym == "a") and self.direction != RIGHT:
            self.direction = LEFT
        elif (event.keysym == "Right" or event.keysym == "d") and self.direction != LEFT:
            self.direction = RIGHT
        elif event.keysym == "r" and self.game_over:
            self.reset_game()

    def move(self):
        head_x, head_y = self.snake[0]
        if self.direction == UP:
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == LEFT:
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == RIGHT:
            new_head = (head_x + GRID_SIZE, head_y)

        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            self.snake[0] in self.snake[1:]
        ):
            self.game_over = True

    def update(self):
        if not self.game_over:
            self.move()
            self.check_collision()
            self.canvas.delete(tk.ALL)
            
            # Dibujar la serpiente
            for segment in self.snake:
                self.canvas.create_rectangle(segment[0], segment[1],
                                             segment[0] + GRID_SIZE, segment[1] + GRID_SIZE,
                                             fill=SNAKE_COLOR)
            
            # Dibujar la comida
            self.canvas.create_rectangle(self.food[0], self.food[1],
                                         self.food[0] + GRID_SIZE, self.food[1] + GRID_SIZE,
                                         fill=FOOD_COLOR)
            
            # Mostrar puntaje
            self.canvas.create_text(20, 20, text=f"Score: {self.score}", anchor=tk.NW)

            self.window.after(SNAKE_SPEED, self.update)
        else:
            self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text=f"Game Over\nScore: {self.score}", anchor=tk.CENTER)

# Crear la ventana del juego
root = tk.Tk()
root.title("Snake Game")
game = SnakeGame(root)

root.mainloop()
