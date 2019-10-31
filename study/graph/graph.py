import sys

# Ugly hack is ugly :-(
from os.path import dirname as dir
sys.path.append(dir(sys.path[0]))
__package__ = "priority_queue"
from priority_queue.priority_queue import PriorityQueue

class Graph:
    def __init__(self, *args, **kwargs):
        self.node_mapping = {}
        self.edges = {}

        # n1, n2, n3, etc.
        # edges: (n1,n2): <weight>
        # to easily find neighbors, easiest to including mapping
        # in node set to
        # e.g. n1: [n2, n3] for edges (n1, n2) and (n1, n3)

    def addEdge(self, n1, n2, w):
        """Add edge from node n1 to n2 with weight w
        """
        # add to node mapping
        if n1 in self.node_mapping:
            self.node_mapping[n1].append(n2)
        else:
            self.node_mapping[n1] = [n2]

        # add to edge set
        self.edges[(n1,n2)] = w

    def getEdgeWeight(self, edge):
        return self.edges.get(edge)

    def dijkstra(self, start, end):
        """Returns shortest path from start to end
        """

        # initially set all distances to nodes to be infinite (except for root)
        distances = { start: 0 }

        for node, nodeList in self.node_mapping.items():
            nodes = [node, *nodeList]

            for n in nodes:
                if n not in distances:
                    distances[n] = sys.maxsize

        # initialize priority queue
        # will store (node, distance to node) tuples
        Q = PriorityQueue(lambda n: n[1])
        Q.insert((start, 0))

        while not Q.isEmpty():
            node, distanceToNode = Q.popMin()

            # first check if node has any outgoing edges
            if node not in self.node_mapping:
                continue

            for neighbor in self.node_mapping[node]:
                maybeShortestDistance = distances[node] + self.getEdgeWeight((node, neighbor))

                # if new shortest distance, update + enqueue!
                if maybeShortestDistance < distances[neighbor]:
                    distances[neighbor] = maybeShortestDistance
                    Q.insert((neighbor, maybeShortestDistance))

        return distances

    def __str__(self):
        string = "Node Mapping:\n"
        for node in self.node_mapping:
            string += "{n} => ".format(n=node)
            string += str(self.node_mapping[node]) + "\n"
        
        string += "Edges:\n"
        for edge in self.edges:
            string += "{e1} === {w} ===> {e2}\n".format(e1=edge[0],w=self.edges[edge],e2=edge[1])

        return string
        
def main():
    testG = Graph()
    node_mapping = {
        "a": ["b", "c", "d"],
        "c": ["d"],
        "d": ["f"]
    }

    # generate random edge weights
    for n in node_mapping:
        for neighbor in node_mapping[n]:
            testG.addEdge(n, neighbor, 1)

    print(testG)
    
    # dijkstra's
    distances = testG.dijkstra("a", "f")
    print(distances)

if __name__ == "__main__":
    main()