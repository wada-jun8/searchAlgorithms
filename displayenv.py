#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from grid_env import GridEnv  # 提供されたgrid_env.pyをインポート

def plot_environment(grid: list, start: tuple, goal: tuple):
    """
    グリッド環境、スタート、ゴールのみを可視化する関数。
    """
    grid_disp = np.array(grid)
    plt.figure(figsize=(8, 8))
    
    # カスタムカラーマップを作成 (0: 白, 1: 黒)
    cmap = ListedColormap(['white', 'black'])
    
    # グリッドを描画
    plt.imshow(grid_disp, cmap=cmap, origin='upper')

    # スタート地点（緑の円）とゴール地点（赤の星）をプロット
    plt.plot(start[1], start[0], 'go', markersize=12, markeredgecolor='k', label='Start')
    plt.plot(goal[1], goal[0], 'bo', markersize=12, markeredgecolor='k', label='Goal')
    
    # グリッド線を表示
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, len(grid[0]), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(grid), 1), minor=True)
    ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.legend()
    plt.title('Grid Environment')
    plt.show()

def main():
    """
    メイン関数
    """
    # グリッド環境のパラメータ（自由に変更してください）
    WIDTH = 15
    HEIGHT = 15
    OBSTACLE_RATIO = 0.25
    SEED = 42  # 固定したい場合は整数、ランダムにする場合はNone

    # GridEnvのインスタンスを作成
    env = GridEnv(width=WIDTH, height=HEIGHT, obstacle_ratio=OBSTACLE_RATIO, seed=SEED)
    grid = env.get_grid()
    start, goal = env.get_start_goal()

    # 環境の情報を表示
    num_obstacles = sum(row.count(1) for row in grid)
    print(f"Grid Size: {WIDTH}x{HEIGHT}")
    print(f"Obstacle Ratio: {OBSTACLE_RATIO:.2f}")
    print(f"Number of Obstacles: {num_obstacles}")
    print(f"Start: {start}")
    print(f"Goal: {goal}")

    # 環境を描画
    plot_environment(grid, start, goal)

if __name__ == '__main__':
    main()
