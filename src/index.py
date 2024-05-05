# This is my home.

from flask import Flask
from markupsafe import escape
from collections import deque
from sol import hello


app = Flask(__name__)

contries = [0, 1, 2, 3, 5, 7]

# flask --app index run


# Function to perform Breadth First Search on a graph
# represented using adjacency list


def bfs(adjList, startNode, visited):
    # Create a queue for BFS
    q = deque()

    # Mark the current node as visited and enqueue it
    visited[startNode] = True
    q.append(startNode)

    # Iterate over the queue
    while q:
        # Dequeue a vertex from queue and print it
        currentNode = q.popleft()
        print(currentNode, end=" ")

        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent has not been visited, then mark it visited and enqueue it
        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

# Function to add an edge to the graph


def addEdge(adjList, u, v):
    adjList[u].append(v)


def main():
    # Number of vertices in the graph
    vertices = 5

    # Adjacency list representation of the graph
    adjList = [[] for _ in range(vertices)]

    # Add edges to the graph
    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 2, 4)

    # Mark all the vertices as not visited
    visited = [False] * vertices

    # Perform BFS traversal starting from vertex 0
    lstr = 'Breadth First Traversal starting from vertex 0: ' + vertices
    bfs(adjList, 0, visited)
    return lstr


if __name__ == "__main__":
    main()


@app.route("/")
def hello_world():
    return f'<h1>Breadth first search</h1><h3>{hello()}</h3><br><p>{main()}</p>'
