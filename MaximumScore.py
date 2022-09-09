from typing import List, Tuple, Optional

import heapq
import math

class RoadGraph:
    def __init__(self, roads, cafes):
        self.roads = roads
        self.cafes = cafes
        self.graph = self.create_graph(roads, cafes)
        self.distances = self.dijkstra(self.graph, 0)
        self.cafe_distances = self.get_cafe_distances(self.distances, cafes)

    def create_graph(self, roads, cafes):
        graph = {}
        for road in roads:
            if road[0] not in graph:
                graph[road[0]] = []
            if road[1] not in graph:
                graph[road[1]] = []
            graph[road[0]].append((road[1], road[2]))
            graph[road[1]].append((road[0], road[2]))
        for cafe in cafes:
            if cafe[0] not in graph:
                graph[cafe[0]] = []
            graph[cafe[0]].append((cafe[0], cafe[1]))
        return graph

    def dijkstra(self, graph, start):
        distances = {}
        for vertex in graph:
            distances[vertex] = math.inf
        distances[start] = 0
        queue = []
        heapq.heappush(queue, (0, start))
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return distances

    def get_cafe_distances(self, distances, cafes):
        cafe_distances = {}
        for cafe in cafes:
            cafe_distances[cafe[0]] = distances[cafe[0]]
        return cafe_distances

def optimalRoute(downhillScores: List[Tuple[int, int, int]], start: int, finish: int) -> Optional[List[int]]:
    # Your code goes here
    roads = []
    cafes = []
    for downhillScore in downhillScores:
        roads.append((downhillScore[0], downhillScore[1], downhillScore[2]))
    roads.append((start, finish, 0))
    roads.append((finish, start, 0))
    graph = RoadGraph(roads, cafes)
    distances = graph.distances
    if distances[finish] == math.inf:
        return None
    path = [finish]
    current = finish
    while current != start:
        for neighbor, weight in graph.graph[current]:
            if distances[current] - weight == distances[neighbor]:
                path.append(neighbor)
                current = neighbor
                break
    return path[::-1]

if __name__ == "__main__":
    downhillScores = [(0, 6, -500), (1, 4, 100), (1, 2, 300), (6, 3, -100), (6, 1, 200), (3, 4, 400), (3, 1, 400), (5, 6, 700), (5, 1, 1000), (4, 2, 100)]
    start = 6
    finish = 2
    print(optimalRoute(downhillScores, start, finish))