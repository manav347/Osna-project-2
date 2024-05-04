import pandas as pd
import networkx as nx
import community  # python-louvain

# Read the Excel file
df = pd.read_excel("final.xlsx")

# Create a graph from the DataFrame
G = nx.from_pandas_edgelist(df, "Source", "Target")

# Detect communities in the graph using Louvain method
partition = community.best_partition(G)

# Print the communities
for com in set(partition.values()):
    print(f"Community {com}:")
    members = [str(nodes) for nodes in partition.keys() if partition[nodes] == com]
    print(', '.join(members))
    print()
