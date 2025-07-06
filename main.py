#! /usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from grid_env import GridEnv
import search_algorithms as sa
import numpy as np
from matplotlib.colors import ListedColormap
import csv

ALGOS = [
    ("A*", sa.astar),
    ("Dijkstra", sa.dijkstra),
    ("BFS", sa.bfs),
    ("DFS", sa.dfs),
    ("Greedy", sa.greedy),
]
COLORS = ['red', 'blue', 'green', 'purple', 'orange']
NODE_COLORS = ['#ffcccc', '#ccccff', '#ccffcc', '#e0ccff', '#ffe0b3']  # 薄い色


def plot_grid_single(grid, path, start, goal, algo_name, color, info, visited_set):
    grid_disp = np.array([[1 if cell == 1 else 0 for cell in row] for row in grid])
    plt.figure()
    # カスタムカラーマップで障害物を黒に
    cmap = ListedColormap(['white', 'black'])  # 0:白, 1:黒
    plt.imshow(grid_disp, cmap=cmap, origin='upper')
    ax = plt.gca()
    # 計算したノードを薄い色で塗る（障害物以外）
    if visited_set:
        for (vx, vy) in visited_set:
            if grid[vx][vy] == 0:
                ax.add_patch(Rectangle((vy-0.5, vx-0.5), 1, 1, color=color, alpha=0.2, zorder=1))
    # 経路
    if path:
        px, py = zip(*path)
        plt.plot(py, px, marker='o', color=color, label='Path', zorder=3)
    plt.plot(start[1], start[0], 'go', label='Start', zorder=4)
    plt.plot(goal[1], goal[0], 'bo', label='Goal', zorder=4)
    plt.legend()
    plt.title(f'{algo_name} \nPathLen:{info["path_length"]} Nodes:{info["visited_nodes"]} Loops:{info["loop_count"]} Time:{info["time"]:.5f}s')
    plt.show(block=False)

def main():
    env = GridEnv(width=15, height=15, obstacle_ratio=0.2, seed=None)  # seed=Noneで毎回ランダム
    grid = env.get_grid()
    start, goal = env.get_start_goal()
    # 障害物の数を計算して表示
    num_obstacles = sum(cell == 1 for row in grid for cell in row)
    print(f'障害物の数: {num_obstacles}')
    for idx, ((name, algo), color) in enumerate(zip(ALGOS, COLORS)):
        path, info = algo(grid, start, goal)
        visited_set = info.get('visited_set', set())
        goal_reached = 1 if path is not None else 0
        print(f'{name}: goal_reached={goal_reached}, path length={info["path_length"]}, nodes={info["visited_nodes"]}, loops={info["loop_count"]}, time={info["time"]:.5f}s')
        if goal_reached == 1:
            filename = f'result_{name.replace("*", "star")}.csv'
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["algorithm", "goal_reached", "path_length", "nodes", "loops", "time"])
                writer.writerow([name, goal_reached, info["path_length"], info["visited_nodes"], info["loop_count"], info["time"]])
        plot_grid_single(grid, path, start, goal, name, color, info, visited_set)
    plt.show()

if __name__ == '__main__':
    main() 