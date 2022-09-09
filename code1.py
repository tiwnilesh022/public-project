class RoadGraph:
    # graph Constructor
    def __init__(self, roads):

        n = len(roads)
        # implement adjacency list
        self.adjList = [None] * n

        # create adjacency list for each above adjacency list
        for i in range(n):
            self.adjList[i] = []

        # add edges to the directed graph
        for (u, v, w) in roads:
            # allocate node in adjacency list from src to dest
            self.adjList[u].append((v, w))


# PrintGraph is the Function for printing adjacency list representation of a graph
def printGraph(graph):
    for u in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for (v, w) in graph.adjList[u]:
            print(f'({u} —> {v}, {w}) ', end='')
        print()


if __name__ == '__main__':

    roads = [(0, 1, 4), (0, 3, 2), (0, 2, 3), (2, 3, 2), (3, 0, 3)]

    # construct the structure of the graph
    mygraph_constructed = RoadGraph(roads)

    # displaing the adjacency list representation of the graph
    printGraph(mygraph_constructed)  # (u->v, weight) representation
