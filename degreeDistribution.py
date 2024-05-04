import pandas as pd
import networkx as nx
from statistics import mean, median, mode

import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel("final.xlsx")

# Create a graph from the DataFrame
G = nx.from_pandas_edgelist(df, "Source", "Target")

# Compute the degree of nodes
degrees = [degree for node, degree in G.degree()]

# Compute mean, median, mode, and highest degree
mean_degree = mean(degrees)
median_degree = median(degrees)
try:
    mode_degree = mode(degrees)
except StatisticsError:  # If no unique mode exists
    mode_degree = None
highest_degree = max(degrees)

print("Mean degree:", mean_degree)
print("Median degree:", median_degree)
print("Mode degree:", mode_degree)
print("Highest degree:", highest_degree)



# Read the Excel file
df = pd.read_excel("final.xlsx")

# Create a graph from the DataFrame
G = nx.from_pandas_edgelist(df, "Source", "Target")

# Compute the degree of nodes
degrees = [degree for node, degree in G.degree()]

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(degrees, bins=20, color='skyblue', edgecolor='black')
plt.title('Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()