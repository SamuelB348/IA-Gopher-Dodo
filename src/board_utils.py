import random
from types_constants import *
from hex_tools import *


class BoardUtils:
    def __init__(self, hex_size: int, state: State):
        self.size = hex_size
        self.CELLS = self.generate_cells(self.size)
        self.R_POV_NEIGHBORS = self.generate_neighbors([1, 2, 3])
        self.B_POV_NEIGHBORS = self.generate_neighbors([0, 4, 5])
        self.CELL_KEYS, self.TURN_KEY = self.generate_zobrist_keys()
        self.start_hash = self.compute_start_hash(state)

    @staticmethod
    def generate_cells(hex_size: int) -> CellSet:
        cells = set()
        n = hex_size - 1
        for r in range(n, -n - 1, -1):
            q1 = max(-n, r - n)
            q2 = min(n, r + n)
            for q in range(q1, q2 + 1):
                cells.add(Cell(q, r))
        return cells

    def generate_neighbors(self, directions: list[int]) -> Neighbors:
        return {
            cell: [
                neighbor(cell, i) for i in directions if neighbor(cell, i) in self.CELLS
            ]
            for cell in self.CELLS
        }

    def generate_zobrist_keys(self):
        cell_keys = {}
        used_keys = set()

        def generate_unique_key():
            key = random.getrandbits(64)
            while key in used_keys:
                key = random.getrandbits(64)
            used_keys.add(key)
            return key

        for cell in self.CELLS:
            key_r = generate_unique_key()
            key_b = generate_unique_key()
            cell_keys[cell] = zkey(key_r, key_b)

        return cell_keys, generate_unique_key()

    def compute_start_hash(self, state: State):
        start_hash = 0
        for (cell, player) in state:
            if player == R:
                start_hash ^= self.CELL_KEYS[cell].R
            else:
                start_hash ^= self.CELL_KEYS[cell].B
        return start_hash

    def state_to_dict(self, state: State):
        grid = {}
        n = self.size - 1
        for r in range(n, -n - 1, -1):
            q1 = max(-n, r - n)
            q2 = min(n, r + n)
            for q in range(q1, q2 + 1):
                if (Cell(q, r), R) in state:
                    grid[Cell(q, r)] = R
                elif (Cell(q, r), B) in state:
                    grid[Cell(q, r)] = B
                else:
                    grid[Cell(q, r)] = 0
        return grid
