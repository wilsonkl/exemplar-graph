# exemplar-graph
Empirical experiments for sampling form concentrated distributions on a space of graphs

# Overview
**This is experimental code for an active research project. No effort has been made to prepare it for release or broader use.**

The goal of this project is to develop a concentrated probability distribution on a space of random graphs, along with a procedure for sampling from that distribution. We envision the research producing:
1. a sampling procedure for producing a new random graph from a given exemplar
2. a simple description of a concentrated probability distribution, which the procedure samples from

A probability distribution should depend on some notion of distance on a space of graphs. We are aiming for a distribution that tends to preserve global graph structure, probably understood in a spectral sense.

# Notes on the code
Everything here is in Python 3. See `requirements.txt` for a list of dependencies, or just install them in the usual way:
```
python -m pip install -r requirements.txt
```
Also, all of the files that are intended to be executable targets live in the `experiments` folder. They are intended to be run from the root level folder of this project.
