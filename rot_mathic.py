import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_next_position(r, c):
    mapping = {
        (0, 0): (1, 0),
        (1, 0): (2, 0),
        (2, 0): (2, 1),
        (2, 1): (2, 2),
        (2, 2): (1, 2),
        (1, 2): (0, 2),
        (0, 2): (0, 1),
        (0, 1): (0, 0)
    }
    return mapping.get((r, c), (r, c))

letters = {
    'R': (0, 0),
    'T': (2, 2),
    'O': (1, 1)
}

while True:
    clear()
    
    grid = [[' ' for _ in range(3)] for _ in range(3)]
    for letter, (r, c) in letters.items():
        grid[r][c] = letter
    
    for row in grid:
        print("   ".join(row))
    
    for letter in ['R', 'T']:
        r, c = letters[letter]
        letters[letter] = get_next_position(r, c)
    
    time.sleep(0.3)