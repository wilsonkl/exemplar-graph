# project layout: experiments are intended to be called from the project
# root level. Put the calling dir on the module path so that project
# modules can be found.
import sys, os
sys.path.append(os.getcwd())

import random
import networkx as nx
import numpy as np
import spectralgraphdistance

"""
Experiment (Monday July 12, 2021)
Let's visualize my proposed spectral graph distance.
(i.e., the spectral radius of the difference of the unweighted
graph Laplacian matrices). I'll use the standard Zack's Karate
Club graph as a starting point and I'll randomly produce one-
edge perturbations. Then compute distances and summarize.

Results:
Oof. I should have seen this coming. All one-edge perturbations
of the graph are distance 2 away. That's because the subtraction
L1 - L2 cancels out all of the terms in the graph Laplacians 
except the four entries related to the edge of interest.
"""

def experiment():
    G = nx.karate_club_graph()

    # repeated experiment: delete or add an edge. Compare to original graph.
    for _ in range(10):
        G2 = G.copy()
        a, b = random.sample(list(G.nodes()), 2) # list, because sampling from set is deprecated?
        print(a, b)
        if G2.has_edge(a,b):
            G2.remove_edge(a, b)
        G2.add_edge(a, b)

        d = spectralgraphdistance.spectralgraphdistance(G, G2)
        print('distance:', d)

if __name__ == '__main__':
    experiment()
