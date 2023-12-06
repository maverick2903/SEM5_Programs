
import random

class WumpusWorldAgent:
    def __init__(self, size):
        self.size = size
        self.visited = [[False] * size for _ in range(size)]
        self.current_location = (0, 0)
    
    def move(self, direction):
        x, y = self.current_location
        if direction == 'up' and x > 0:
            self.current_location = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.current_location = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.current_location = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.current_location = (x, y + 1)
    
    def explore(self):
        while True:
            self.visited[self.current_location[0]][self.current_location[1]] = True
            print(f"Current Location: {self.current_location}")
            
            if self.check_for_gold():
                print("Agent found the gold!")
                break
            
            safe_moves = self.get_safe_moves()
            if not safe_moves:
                print("Agent is trapped or couldn't find the gold.")
                break
            
            next_move = random.choice(safe_moves)
            self.move(next_move)
    
    def check_for_gold(self):
        x, y = self.current_location
        # Simulating the presence of gold at coordinates (size-1, size-1)
        return x == self.size - 1 and y == self.size - 1
    
    def get_safe_moves(self):
        x, y = self.current_location
        safe_moves = []
        
        # Check and add safe moves
        if x > 0 and not self.visited[x - 1][y]:
            safe_moves.append('up')
        if x < self.size - 1 and not self.visited[x + 1][y]:
            safe_moves.append('down')
        if y > 0 and not self.visited[x][y - 1]:
            safe_moves.append('left')
        if y < self.size - 1 and not self.visited[x][y + 1]:
            safe_moves.append('right')
        
        return safe_moves

# Create a Wumpus World agent with a 4x4 grid
agent = WumpusWorldAgent(size=4)

# Start exploring the world
agent.explore()