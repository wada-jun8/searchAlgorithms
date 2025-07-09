#! /usr/bin/env python3

import heapq
from collections import deque
from typing import List, Tuple, Optional
import time

def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(grid, pos):
    h, w = len(grid), len(grid[0])
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
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
    t0 = time.time()
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    cost_so_far = {start: 0}
    visited_nodes = set()
    calc_nodes = []
    loop_count = 0
    while open_list:
        _, g, current = heapq.heappop(open_list)
        loop_count += 1
        visited_nodes.add(current)
        calc_nodes.append(current)
        if current == goal:
            t1 = time.time()
            path = reconstruct_path(came_from, current)
            return path, {
                'loop_count': loop_count,
                'visited_nodes': len(visited_nodes),
                'path_length': len(path) if path else 0,
                'time': t1-t0,
                'visited_set': visited_nodes,
                'calc_nodes': calc_nodes
            }
        for neighbor in get_neighbors(grid, current):
            new_cost = g + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    t1 = time.time()
    return None, {'loop_count': loop_count, 'visited_nodes': len(visited_nodes), 'path_length': 0, 'time': t1-t0, 'visited_set': visited_nodes, 'calc_nodes': calc_nodes}

def dijkstra(grid, start, goal):
    t0 = time.time()
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}
    visited_nodes = set()
    calc_nodes = []
    loop_count = 0
    while open_list:
        g, current = heapq.heappop(open_list)
        loop_count += 1
        visited_nodes.add(current)
        calc_nodes.append(current)
        if current == goal:
            t1 = time.time()
            path = reconstruct_path(came_from, current)
            return path, {
                'loop_count': loop_count,
                'visited_nodes': len(visited_nodes),
                'path_length': len(path) if path else 0,
                'time': t1-t0,
                'visited_set': visited_nodes,
                'calc_nodes': calc_nodes
            }
        for neighbor in get_neighbors(grid, current):
            new_cost = g + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_list, (new_cost, neighbor))
                came_from[neighbor] = current
    t1 = time.time()
    return None, {'loop_count': loop_count, 'visited_nodes': len(visited_nodes), 'path_length': 0, 'time': t1-t0, 'visited_set': visited_nodes, 'calc_nodes': calc_nodes}

def bfs(grid, start, goal):
    t0 = time.time()
    queue = deque([start])
    came_from = {}
    visited = set([start])
    calc_nodes = []
    loop_count = 0
    while queue:
        current = queue.popleft()
        loop_count += 1
        calc_nodes.append(current)
        if current == goal:
            t1 = time.time()
            path = reconstruct_path(came_from, current)
            return path, {
                'loop_count': loop_count,
                'visited_nodes': len(visited),
                'path_length': len(path) if path else 0,
                'time': t1-t0,
                'visited_set': visited,
                'calc_nodes': calc_nodes
            }
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                came_from[neighbor] = current
    t1 = time.time()
    return None, {'loop_count': loop_count, 'visited_nodes': len(visited), 'path_length': 0, 'time': t1-t0, 'visited_set': visited, 'calc_nodes': calc_nodes}

def dfs(grid, start, goal):
    t0 = time.time()
    stack = [start]
    came_from = {}
    visited = set([start])
    calc_nodes = []
    loop_count = 0
    while stack:
        current = stack.pop()
        loop_count += 1
        calc_nodes.append(current)
        if current == goal:
            t1 = time.time()
            path = reconstruct_path(came_from, current)
            return path, {
                'loop_count': loop_count,
                'visited_nodes': len(visited),
                'path_length': len(path) if path else 0,
                'time': t1-t0,
                'visited_set': visited,
                'calc_nodes': calc_nodes
            }
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                came_from[neighbor] = current
    t1 = time.time()
    return None, {'loop_count': loop_count, 'visited_nodes': len(visited), 'path_length': 0, 'time': t1-t0, 'visited_set': visited, 'calc_nodes': calc_nodes}

def greedy(grid, start, goal):
    t0 = time.time()
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))
    came_from = {}
    visited = set([start])
    calc_nodes = []
    loop_count = 0
    while open_list:
        _, current = heapq.heappop(open_list)
        loop_count += 1
        calc_nodes.append(current)
        if current == goal:
            t1 = time.time()
            path = reconstruct_path(came_from, current)
            return path, {
                'loop_count': loop_count,
                'visited_nodes': len(visited),
                'path_length': len(path) if path else 0,
                'time': t1-t0,
                'visited_set': visited,
                'calc_nodes': calc_nodes
            }
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current
    t1 = time.time()
    return None, {'loop_count': loop_count, 'visited_nodes': len(visited), 'path_length': 0, 'time': t1-t0, 'visited_set': visited, 'calc_nodes': calc_nodes} 