# dronesummer17
Early formulations of an optimal path planning algorithm. Searches down the statespace brute force using a recursive tree search. Honestly, not great performance wise but builds an understanding why path planning is such a difficult problem computationally. Performance could be improved by accounting for path symmetry (eg {[2,1]->[3,1]->[0,0]->[2,1]} is equivalent to {[2,1]->[0,0]->[3,1]->[2,1]}).

- Formulation 2-1: Has multiple drones searching the space at the same time. Really increases the tree width making computation absurdly slow

- Formulation 1-1: Has a single drone searching the space. Pretty fast compared to 2-1.
