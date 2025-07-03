#! /usr/bin/env python3

import random
from typing import List, Tuple

class GridEnv:
    def __init__(self, width: int, height: int, obstacle_ratio: float = 0.2, seed: int = 42):
        self.width = width
        self.height = height
        self.obstacle_ratio = obstacle_ratio
        self.seed = seed
        self.grid = self._generate_grid()
        self.start = (0, 0)
        self.goal = (height - 1, width - 1)

    def _generate_grid(self) -> List[List[int]]:
        random.seed(self.seed)
        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        num_obstacles = int(self.width * self.height * self.obstacle_ratio)
        obstacles = set()
        while len(obstacles) < num_obstacles:
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)
            if (x, y) not in [(0, 0), (self.height - 1, self.width - 1)]:
                obstacles.add((x, y))
        for x, y in obstacles:
            grid[x][y] = 1
        return grid

    def get_grid(self) -> List[List[int]]:
        return self.grid

    def get_start_goal(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return self.start, self.goal 