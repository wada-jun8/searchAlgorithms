import matplotlib.pyplot as plt
from grid_env import GridEnv
import search_algorithms as sa

ALGOS = [
    ("A*", sa.astar),
    ("Dijkstra", sa.dijkstra),
    ("BFS", sa.bfs),
    ("DFS", sa.dfs),
    ("Greedy", sa.greedy),
]
COLORS = ['red', 'blue', 'green', 'purple', 'orange']


def plot_grid_single(grid, path, start, goal, algo_name, color):
    grid_disp = [[1 if cell == 1 else 0 for cell in row] for row in grid]
    plt.figure()
    plt.imshow(grid_disp, cmap='Greys', origin='upper')
    if path:
        px, py = zip(*path)
        plt.plot(py, px, marker='o', color=color, label='Path')
    plt.plot(start[1], start[0], 'go', label='Start')
    plt.plot(goal[1], goal[0], 'bo', label='Goal')
    plt.legend()
    plt.title(f'{algo_name} Result')
    plt.show(block=False)

def main():
    env = GridEnv(width=15, height=15, obstacle_ratio=0.2, seed=42)
    grid = env.get_grid()
    start, goal = env.get_start_goal()
    for (name, algo), color in zip(ALGOS, COLORS):
        path = algo(grid, start, goal)
        print(f'{name} path length:', len(path) if path else 'No path')
        plot_grid_single(grid, path, start, goal, name, color)
    plt.show()

if __name__ == '__main__':
    main() 