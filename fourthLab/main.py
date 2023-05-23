import random
import time
import matplotlib.pyplot as plt
import networkx as nx

# Balanced graph 1
graph_1 = nx.Graph()
graph_1.add_edges_from([(0, 1), (1, 6), (6, 5), (5, 9),
                       (9, 8), (8, 7), (7, 2), (2, 3), (3, 4), (4, 0)])
# Balanced graph 2
graph_2 = nx.Graph()

graph_2.add_nodes_from(range(10))
for node in range(10):
    neighbors = [(node + i) % 10 for i in range(2, 6)]
    graph_2.add_edges_from([(node, neighbor) for neighbor in neighbors])

# Unbalanced graph 1
graph_3 = nx.Graph()

graph_3.add_nodes_from(range(10))
degrees = [1, 2, 3, 4] * 3 + [1]
for i in range(10):
    degree = degrees[i]
    neighbors = []
    while len(neighbors) < degree:
        neighbor = (i + len(neighbors) + 1) % 10
        if neighbor not in neighbors:
            neighbors.append(neighbor)
    graph_3.add_edges_from([(i, neighbor) for neighbor in neighbors])

# Unbalanced graph 2
graph_4 = nx.Graph()
graph_4.add_edges_from([(0, 1), (1, 2), (1, 4), (1, 6), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (
    3, 8), (3, 9), (4, 1), (4, 2), (4, 7), (4, 8), (5, 2), (6, 2), (6, 3), (7, 1), (7, 4), (7, 3), (7, 8), (8, 9), (9, 2)])


def run_dfs(G, start_node, stop_node):
    start_time = time.time()
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node == stop_node:
            end_time = time.time()
            return end_time - start_time
        if node not in visited:
            visited.add(node)
            stack.extend(reversed(list(G.neighbors(node))))
    end_time = time.time()
    return end_time - start_time


def run_bfs(G, start_node, stop_node):
    start_time = time.time()
    visited = set()
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node == stop_node:
            end_time = time.time()
            return end_time - start_time
        if node not in visited:
            visited.add(node)
            queue.extend(list(G.neighbors(node)))
    end_time = time.time()
    return end_time - start_time


# Draw the graphs
plt.subplot(2, 2, 1)
nx.draw(graph_1, with_labels=True)
plt.title("Graph 1")

plt.subplot(2, 2, 2)
nx.draw(graph_2, with_labels=True)
plt.title("Graph 2")

plt.subplot(2, 2, 3)
nx.draw(graph_3, with_labels=True)
plt.title("Graph 3")

plt.subplot(2, 2, 4)
nx.draw(graph_4, with_labels=True)
plt.title("Graph 4")

plt.show()

# Run the DFS and BFS searches
start_node = random.randint(0, 9)
stop_node = start_node

while stop_node == start_node:
    stop_node = random.randint(0, 9)

print("Start node:", start_node, "\nStop node:", stop_node)

results = []

for i, G in enumerate([graph_1, graph_2, graph_3, graph_4], start=1):
    dfs_time = run_dfs(G, start_node, stop_node)
    bfs_time = run_bfs(G, start_node, stop_node)
    results.append((i, dfs_time, bfs_time))

# Print the results table
print("Results Table:")
print("{:<10} {:<15} {:<15}".format("Graph", "DFS Time", "BFS Time"))

for graph_num, dfs_time, bfs_time in results:
    print("{:<10} {:<15.6f} {:<15.6f}".format(graph_num, dfs_time, bfs_time))

# Create a line chart of the results
graph_labels = ["Graph {}".format(i) for i in range(1, 5)]
dfs_times = [result[1] for result in results]
bfs_times = [result[2] for result in results]

x_pos = [i for i, _ in enumerate(graph_labels)]
plt.plot(x_pos, dfs_times, '-o', color="blue")
plt.plot(x_pos, bfs_times, '-o', color="red")

plt.xlabel("Graph")
plt.ylabel("Execution Time (Seconds)")
plt.title("DFS and BFS Execution Times by Graph")

plt.xticks(x_pos, graph_labels)

plt.legend(["DFS", "BFS"])

plt.show()


# test
