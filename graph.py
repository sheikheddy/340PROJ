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

if __name__ == "__main__":
    main()