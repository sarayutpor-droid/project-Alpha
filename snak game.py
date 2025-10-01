import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - งูสีชมพู")
        self.width = 400
        self.height = 400
        self.cell_size = 20
        self.direction = 'Right'
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = None
        self.score = 0
        self.game_over = False
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.root.bind('<Up>', lambda e: self.change_direction('Up'))
        self.root.bind('<Down>', lambda e: self.change_direction('Down'))
        self.root.bind('<Left>', lambda e: self.change_direction('Left'))
        self.root.bind('<Right>', lambda e: self.change_direction('Right'))
        self.create_food()
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, new_direction):
        opposite = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
        if new_direction != opposite.get(self.direction):
            self.direction = new_direction

    def move(self):
        x, y = self.snake[0]
        if self.direction == 'Up':
            y -= self.cell_size
        elif self.direction == 'Down':
            y += self.cell_size
        elif self.direction == 'Left':
            x -= self.cell_size
        elif self.direction == 'Right':
            x += self.cell_size
        new_head = (x, y)
        if (
            x < 0 or x >= self.width or
            y < 0 or y >= self.height or
            new_head in self.snake
        ):
            self.game_over = True
            return
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.create_food()
        else:
            self.snake.pop()

    def update(self):
        if not self.game_over:
            self.move()
            self.draw()
            self.root.after(100, self.update)
        else:
            self.canvas.create_text(self.width//2, self.height//2, text=f"Game Over! Score: {self.score}", font=("Arial", 20), fill="red")

    def draw(self):
        self.canvas.delete('all')
        # Draw snake (pink)
        for i, (x, y) in enumerate(self.snake):
            color = '#FF69B4'  # Hot pink
            self.canvas.create_rectangle(x, y, x+self.cell_size, y+self.cell_size, fill=color, outline='')
        # Draw food
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+self.cell_size, fy+self.cell_size, fill='green', outline='')
        # Draw score
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", font=("Arial", 14), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
