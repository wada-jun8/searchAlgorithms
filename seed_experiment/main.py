#! /usr/bin/env python3

from grid_env import GridEnv
import search_algorithms as sa
import csv
import os

ALGOS = [
    ("A*", sa.astar),
    ("Dijkstra", sa.dijkstra),
    ("BFS", sa.bfs),
    ("DFS", sa.dfs),
    ("Greedy", sa.greedy),
]

def main():
    width, height, obstacle_ratio = 15, 15, 0.2
    for name, algo in ALGOS:
        filename = f'result_{name.replace("*", "star")}.csv'
        # ヘッダーを書き込む（ファイルがなければ）
        if not os.path.exists(filename):
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["seed", "goal_reached", "path_length", "nodes", "loops", "time"])
        for seed in range(1,100001):
            env = GridEnv(width=width, height=height, obstacle_ratio=obstacle_ratio, seed=seed)
            grid = env.get_grid()
            start, goal = env.get_start_goal()
            path, info = algo(grid, start, goal)
            # pathがNoneでなく、かつlen(path)>0ならgoal_reached=1
            if path is not None and len(path) > 0:
                goal_reached = 1
            else:
                goal_reached = 0
            if goal_reached == 1:
                with open(filename, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([seed, goal_reached, info["path_length"], info["visited_nodes"], info["loop_count"], info["time"]])

if __name__ == '__main__':
    main() 