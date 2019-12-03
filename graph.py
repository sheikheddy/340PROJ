#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:21:54 2019

@author: sheikh
"""

import networkx as nx
import matplotlib.pyplot as plt
#import math
import csv
#import random as rand
import sys

def buildG(G, file_, delimiter_):
    #construct the weighted version of the contact graph from cgraph.dat file
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        if float(line[2]) != 0.0:
            G.add_edge(int(line[0]),int(line[1]),weight=float(line[2]))

# Adjacency list representation of a graph            
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def main():
    graph_fn="tempset3.txt";
    G = nx.Graph()  #let's create the graph first
    buildG(G, graph_fn, ',')

    print(G.nodes())
    print(G.number_of_nodes())

    #nx.draw(G)
    #plt.show(G)

    n = G.number_of_nodes()
    print ("no of nodes: ", n)
    comps=nx.connected_components(G)
    for comp in comps:
        print(comp)
        

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

if __name__ == "__main__":
    main()