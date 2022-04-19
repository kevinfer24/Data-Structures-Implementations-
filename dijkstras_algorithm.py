# Kevin Fernandez
# April 19, 2022

# Simple implementation of Dijkstra's algorithm.

# Graphs
import math

class WeightedGraph:
    # Constructor
    def __init__(self) -> None:
        self.vertices = []
        self.adjacency_list = {}
        self.weights = {}
    
    def build_from_adjacency_list( aList, wList):
        G = WeightedGraph()
        for index, (v, adjV) in enumerate(aList):
            if v not in G.vertices:
                G.vertices.append(v)
            if adjV not in G.vertices:
                G.vertices.append(adjV)
            try:
                G.adjacency_list[v].append(adjV)
                G.weights[(v, adjV)] = wList[index]
            except:
                # if doesnt exist, just make it with one
                G.adjacency_list[v] = [adjV]
                G.weights[(v, adjV)] = wList[index]

            try:
                G.adjacency_list[adjV].append(v)
                G.weights[(adjV, v)] = wList[index]
            except:
                # if doesnt exist, just make it with one
                G.adjacency_list[adjV] = [v]
                G.weights[(adjV, v)] = wList[index]
        return G
    
    def dijkstra(self, start):
        # Make empty visited set, fill unvisited set.
        # distance and last_vert dictionaries/maps act as the columns
        visited = []
        unvisited = self.vertices.copy()
        distance = {}
        last_vert = {}
        for vert in unvisited:
            distance[vert] = math.inf
        distance[start] = 0
        last_vert[start] = 'n/a'
        current_vert = start

        # Begin Looping
        while len(unvisited) > 0:
            # Explore neighbors
            for neighbor in self.adjacency_list[current_vert]:
                if neighbor not in visited:
                    weight = self.weights[(current_vert, neighbor)]
                    if distance[current_vert] + weight < distance[neighbor]:
                        distance[neighbor] = distance[current_vert] + weight
                        last_vert[neighbor] = current_vert
            visited.append(current_vert)
            unvisited.remove(current_vert)
            # Pick next vert to visit
            smallest = math.inf
            for vert in unvisited:
                if distance[vert] < smallest:
                    smallest = distance[vert]
                    current_vert = vert
        
        return distance, last_vert


#------------------------------------------------------------
# Test

Cities = WeightedGraph.build_from_adjacency_list([
    ('a', 'b'), ('a', 'd'), ('b', 'c'), ('b', 'e'), ('d', 'e'), ('c', 'z'), ('e', 'z')], 
    [4, 2, 3, 3, 3, 2, 1])

a_distances, last_verts = Cities.dijkstra('a')

for item in a_distances.items():
    print(item)