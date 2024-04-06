# Install graphframes library using %pip magic command
%pip install graphframes

# Import required modules
from graphframes import GraphFrame
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("SocialNetworkAnalysis").getOrCreate()

# Define vertices (users) and edges (friendships)
vertices = spark.createDataFrame([
    ("Alice", "Person"),
    ("Bob", "Person"),
    ("Charlie", "Person"),
    ("David", "Person"),
    ("Emma", "Person")
], ["id", "type"])

edges = spark.createDataFrame([
    ("Alice", "Bob", "friend"),
    ("Bob", "Charlie", "friend"),
    ("Charlie", "David", "friend"),
    ("David", "Emma", "friend"),
    ("Emma", "Alice", "friend")
], ["src", "dst", "relationship"])

# Create a GraphFrame
graph = GraphFrame(vertices, edges)

# Display the vertices and edges of the graph
print("Vertices:")
graph.vertices.show()

print("Edges:")
graph.edges.show()

# Calculate the in-degree of each vertex (number of incoming connections)
inDegrees = graph.inDegrees
print("In-degree of each vertex:")
inDegrees.show()

# Find the most connected users (highest in-degree)
mostConnectedUsers = inDegrees.orderBy("inDegree", ascending=False)
print("Top 3 most connected users:")
mostConnectedUsers.show(3)

# Run PageRank algorithm to determine node importance
pageRankResults = graph.pageRank(resetProbability=0.15, maxIter=10)
print("PageRank results:")
pageRankResults.vertices.show()
