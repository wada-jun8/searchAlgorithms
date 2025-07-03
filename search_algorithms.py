#! /usr/bin/env python3

import heapq
from collections import deque
from typing import List, Tuple, Optional

def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(grid, pos):
    h, w = len(grid), len(grid[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    result = []
    for dx, dy in directions:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0:
            result.append((nx, ny))
    return result

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    cost_so_far = {start: 0}
    while open_list:
        _, g, current = heapq.heappop(open_list)
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(grid, current):
            new_cost = g + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    return None

def dijkstra(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}
    while open_list:
        g, current = heapq.heappop(open_list)
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(grid, current):
            new_cost = g + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_list, (new_cost, neighbor))
                came_from[neighbor] = current
    return None

def bfs(grid, start, goal):
    queue = deque([start])
    came_from = {}
    visited = set([start])
    while queue:
        current = queue.popleft()
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                came_from[neighbor] = current
    return None

def dfs(grid, start, goal):
    stack = [start]
    came_from = {}
    visited = set([start])
    while stack:
        current = stack.pop()
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                came_from[neighbor] = current
    return None

def greedy(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))
    came_from = {}
    visited = set([start])
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current
    return None 