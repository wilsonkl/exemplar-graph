import numpy as np
import networkx as nx


def do_experiment(num_trials, alpha):
   
    results = [one_trial(alpha) for _ in range(num_trials)]
    return results

def one_trial(alpha):
    G = nx.generators.les_miserables_graph()
    Gnew = nx.spectral_graph_forge(G, alpha, transformation='modularity')
    return nx.algebraic_connectivity(Gnew) 
    
if __name__ == '__main__':
    for alpha in np.linspace(0, 1, 11):
        results = do_experiment(num_trials=100, alpha=alpha)
        print(f'alpha: {alpha:2.2f} \tl2 mu: {np.mean(results):3.2g} \tl2 stdev: {np.std(results):3.2g}')
