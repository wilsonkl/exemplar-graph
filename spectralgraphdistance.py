import numpy as np
import networkx as nx
import scipy.sparse.linalg


def spectralgraphdistance(G1, G2):
    """
    Compute the distance between G1 and G2, defined as || L1 - L2 ||_2,
    where L1 and L2 are the unweighted graph Laplacian matrices corresponding
    to G1 and G2, and || . ||_2 is the induced matrix 2-norm, (which is the
    spectral radius for symmetric matrices like ours.) 

    This distance metric assumes that G1 and G2 are defined over the same
    vertex set.
    
    Note: This is all dense matrix math. Of course, sparse matrix work is key
        for larger problem sizes. Cross that bridge if this works and it seems
        worth it. (scipy.sparse.csgraph has a graph laplacian function)

    """
    # Check precondition: same vertex set
    V1 = G1.nodes()
    V2 = G2.nodes()
    if len(set(V1).intersection(set(V2))) != len(V1):
        raise ValueError("graphs G1 and G2 need to have the same vertex set.")
    
    # Get the graph Laplacians. Use the node ordering of G1.
    # need to upcast the type? https://stackoverflow.com/questions/8650014/sparse-matrix-valueerror-matrix-type-must-be-f-d-f-or-d
    L1 = nx.laplacian_matrix(G1, nodelist=V1).asfptype()
    L2 = nx.laplacian_matrix(G2, nodelist=V1).asfptype()
    
    # Compute spectral radius using ARPACK / Lanczos iteration
    lambda_max = scipy.sparse.linalg.eigsh(L1 - L2, k=1, which='LM', return_eigenvectors=False)[0]
    return abs(lambda_max)

def _testcase():
    G1 = nx.gnp_random_graph(20, 0.2)
    G2 = nx.gnp_random_graph(20, 0.2)
    d = spectralgraphdistance(G1, G2)
    print('graph distance:', d)

if __name__ == '__main__':
    _testcase()
