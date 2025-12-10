from time import sleep
from Board import Board
from Solver import Solver

def load_puzzles(filename):
    puzzles = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            numbers = []
            for ch in line:
                if ch in '123456789':
                    numbers.append(int(ch))
                else:
                    numbers.append(0)

            assert len(numbers) == 81, f"Puzzle line must have 81 entries, got {len(numbers)}"
            puzzles.append(Board(numbers.copy()))
    return puzzles


boards = load_puzzles("puzzles.txt")

solved = 0
unique = 0

for i, board in enumerate(boards, start=1):
    solver = Solver(board)
    
    if (solver.solve): solved = solved + 1
    if (solver.is_unique()): unique = unique + 1

print(f"Puzzles: {solved} \n\nsolved={solved}, unique={unique}, non-unique={solved - unique}")
input("Press Enter to exit...")
