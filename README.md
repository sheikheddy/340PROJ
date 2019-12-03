CMP 340 Database Systems Group Project
======================================

This is a mini-project where we find the connected components of a graph using python. It currently uses the networkx library, but we plan to remove this dependency and change to explicit DFS and BFS soon. It is based off of [this stackoverflow question](https://stackoverflow.com/questions/26317775/print-connected-components-of-a-graph-in-python).

The BFS and DFS implementations are from [this blog post](https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/). We assume an undirected unweighted graph with an adjacency list representation. 

## TODO

 - Add graph generator
 - Analyze efficiency of algorithms
 - Currently we can find the entire connected component given a node. The naive way to extend this to finding all connected components in a graph is to repeat BFS/DFS for every node, then find the unique graphs. This is obviously inefficient since if a node belongs to a component discovered before we do not need to run DFS/BFS again. I remember reading an elegant solution to this in a book and will try to find it. It probably involves the discovered flags. Or I could steal it from the networkx source. I haven't decided yet.

## Authors

Sheikh Abdur Raheem Ali

Beesan Ayman Amin Hussain

Anas Kamlani

## Usage

Just run `python3 graph.py` to start the program. Alternatively, use your favorite IDE.

If you'd like to modify the graph, edit tempset3.txt (each entry is in the format source, dest, weight)

## Contact

Please reach me at ali@abdur-raheem.com if you have any questions about the code.

## License 
[MIT](https://choosealicense.com/licenses/mit/)
