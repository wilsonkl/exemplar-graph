import os
import numpy as np
import networkx as nx

"""
testgraphs.py

functions to load an interesting collection of real-world graphs.

TODO: download some other types of graphs (as edgelists) from SNAP.
Write a quick dataloader for them too. These aren't in a common format
so I can't write an automatic bulk downloader.

TODO: load graphs from the SuiteSparse matrix collection? Filter by
binary + symmetric and these are basically graphs in matrix form.
"""

def list_vision_graph_names():
    if not os.path.isdir('data/vision_EG_graphs'):
        raise ValueError('can\'t find the data files at data/vision_EG_graphs. Are you running your script outside the root project directory?')
    return os.listdir('data/vision_EG_graphs')

def load_vision_graph(name):
    EGs_file = f'data/vision_EG_graphs/{name}/EGs.txt'
    if not os.path.isfile(EGs_file):
        raise FileNotFoundError('data file {EGs_file} does not exist.')
    # read the file and extract the graph
    tab_data = np.loadtxt(EGs_file)
    tab_data = tab_data[:,0:2].astype(int)
    G = nx.Graph()
    G.add_edges_from(tab_data)
    
    # restrict to the biggest connected component
    ccs = (G.subgraph(c) for c in nx.connected_components(G))
    G = max(ccs, key=len).copy()
    
    # renumber all the vertices sequentially
    G = nx.convert_node_labels_to_integers(G,first_label=0) 
    
    return G

if __name__ == '__main__':
    # testing harness for this file
    
    # test listing the vision graphs
    print('found these vision graphs:')
    print(list_vision_graph_names())
    print()

    # try loading these graphs
    print('{:<20}|{:>6}{:>8}'.format('Name', 'nodes', 'edges'))
    print('-'*35) 
    for name in list_vision_graph_names():
        G = load_vision_graph(name)
        print('{:<20}|{:>6}{:>8}'.format(name, len(G.nodes), len(G.edges)))
    print('-'*35) 

