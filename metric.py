import pandas as pd
import networkx as nx

# Read the Excel file
df = pd.read_excel("final.xlsx")

# Create a graph from the DataFrame
G = nx.from_pandas_edgelist(df, "Source", "Target")

# Get the top 10 nodes with the highest degree
top_10_nodes = sorted(G.degree(), key=lambda x: x[1], reverse=True)[:10]

# Iterate over the top 10 nodes and their neighbors
for node, degree in top_10_nodes:
    print(f"\nNode: {node}, Degree: {degree}")
    neighbors = list(G.neighbors(node))
    
    # Sort the neighbors based on their degree
    sorted_neighbors = sorted(neighbors, key=lambda x: G.degree(x), reverse=True)
    
    # Print the top 3 highest degree neighbors
    print("Top 3 highest degree neighbors:")
    for i, neighbor in enumerate(sorted_neighbors[:3], start=1):
        neighbor_degree = G.degree(neighbor)
        print(f"{i}. Neighbor: {neighbor}, Degree: {neighbor_degree}")
