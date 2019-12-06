#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:21:54 2019

@author: sheikh
"""

from random import seed
from random import randrange

# Python program to print connected  
# components in an undirected graph 
class Graph: 
      
    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 
                  
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
    
    def BFSUtil(self, temp, v, visited):
        Q = []
        visited[v] = True
        Q.append(v)
        temp.append(v)
        while Q:
            v = Q.pop()
            for i in self.adj[v]:
                if visited[i] == False:
                    visited[i] = True
                    Q.append(i)
                    temp.append(i)
        return temp
                    
        return None
    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self, kind): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                if kind == 'DFS':
                    cc.append(self.DFSUtil(temp, v, visited)) 
                elif kind == 'BFS':
                    cc.append(self.BFSUtil(temp, v, visited))
        return cc 
  
# Driver Code 
if __name__=="__main__": 
      
    # Create a graph given in the above diagram 
    # 5 vertices numbered from 0 to 4 
    SIZE = 10000 # Vertices
    seed(0)
    g = Graph(SIZE); 
    E = 30000 #No. of Edges
    for i in range(E):
        g.addEdge(randrange(SIZE), randrange(SIZE))
    cc = g.connectedComponents(kind='BFS') 
    print("Connected components:") 
    for component in cc:
        print(component)
  