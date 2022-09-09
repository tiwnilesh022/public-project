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

    def routing(self, start, end):
        if start == end:
            return [start]
        if end in self.cafe_distances:
            return [start, end]
        if start in self.cafe_distances:
            return [start, end]
        if start in self.graph and end in self.graph:
            return self.find_shortest_path(start, end)
        return []

    def find_shortest_path(self, start, end):
        queue = []
        heapq.heappush(queue, (0, start, [start]))
        while queue:
            current_distance, current_vertex, path = heapq.heappop(queue)
            if current_vertex == end:
                return path
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if neighbor in self.cafe_distances:
                    distance += self.cafe_distances[neighbor]
                if distance < self.distances[neighbor]:
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (distance, neighbor, new_path))
        return []


if __name__ == "__main__":
    roads = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [2, 3, 7], [3, 4, 4], [4, 5, 5], [4, 6, 4], [5, 6, 8], [5, 7, 6], [6, 7, 1], [6, 8, 2], [7, 8, 3]]
    cafes = [[2, 5], [5, 4], [6, 3], [8, 5]]
    mygraph = RoadGraph(roads, cafes)
    start = 0
    end = 8
    print(mygraph.routing(start, end))