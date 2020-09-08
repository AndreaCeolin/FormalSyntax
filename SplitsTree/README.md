# Formal Syntax and Deep History - SplitsTree
This folder contains the instructions files used in the NeighborNet analysis, through [SplitsTree](https://software-ab.informatik.uni-tuebingen.de/download/splitstree4/welcome.html) (Huson and Bryant 2006).

1. **table.nex**: this file contains the dataset in Nexus format. By opening this file with SplitsTree, you will automatically get a NeighborNet analysis.

2. **scores.txt**: delta scores and q-residuals from the NeighborNet analysis. In order to obtain them, do:
    * Analysis -> Compute Delta Scores
    
3. **delta.py**: this Python3 script creates a barplot of the delta scores derived from the NeighborNet analysis. It requires that you have the package ```matplotlib``` installed. Its syntax is ```python3 delta.py scores.txt```.

4. **qresid.py**: this Python3 script creates a barplot of the q-residuals derived from the NeighborNet analysis. It requires that you have the package ```matplotlib``` installed. Its syntax is ```python3 qresid.py scores.txt```.

5. **splitstree_network.nex**: this is the source Nexus file for the SplitsTree network reported in the Supplementary Material.



