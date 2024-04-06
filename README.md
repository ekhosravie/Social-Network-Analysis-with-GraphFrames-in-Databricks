Social Network Analysis with GraphFrames in Databricks
This repository contains Python code for performing social network analysis on a small-scale social network using GraphFrames in Databricks. GraphFrames is a graph processing library built on Apache Spark, 
allowing for efficient graph-based computations within a Spark environment.

Overview
In this analysis, we represent a social network as a graph where users are vertices and friendships are edges. We leverage GraphFrames to create, 
analyze, and visualize the graph, compute important metrics like vertex in-degrees and node importance (PageRank), and explore community structures within the network.

Prerequisites
To run this analysis, you will need:

Access to a Databricks environment with Apache Spark installed
Python environment compatible with Databricks notebooks
Internet access to install required Python libraries (e.g., GraphFrames)
Setup
Install GraphFrames Library:

Use %pip install graphframes in your Databricks notebook to install the GraphFrames library.
Import Required Modules:

Import necessary modules including GraphFrame and SparkSession to interact with GraphFrames and Apache Spark.
Run the Code:

Copy and paste the provided Python code into your Databricks notebook.
Execute the notebook cells to create the graph, perform graph analytics tasks, and visualize the results.
Code Structure
social_network_analysis.ipynb: Databricks notebook containing the code for social network analysis using GraphFrames.
Code Details
Define Vertices and Edges:

Vertices represent users with associated attributes (e.g., user ID and type).
Edges represent friendships between users (source, destination, and relationship type).
Graph Analytics Tasks:

Display basic graph information, including vertices and edges.
Calculate vertex in-degrees to identify highly connected users.
Run the PageRank algorithm to determine node importance in the social network.
Results
The analysis provides insights into the structure of the social network, highlighting influential users and community structures based on graph analytics.
Usage
Feel free to customize the analysis by:

Modifying the size and attributes of the synthetic social network dataset.
Adding additional graph algorithms (e.g., connected components, motif finding) to explore different aspects of the network.
