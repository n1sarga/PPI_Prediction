# PPI_Prediction_Maize

## Dataset Description
* Plant Name: ***Zea mays (Maize)***
* Dataset Size: ***101,869 &times; 3***
* Online Repository: ***IntAct***
* Interaction Types: ***Positive and Negative Interactions***

## Script Description
***[Important]***
* ***seq.py*** script collects protein sequences against each UniProt Protein Identifier using ***UniProt REST-API***.
* ***bipartite_graph.py*** script generates the non-interacting protein combination from positive interactions.
* ***./Scripts/Pre-Process/PSSM.py*** generates the PSSM profiles against each protein sequence. ***PSSM Profiles*** in ***parquet*** format has been added in this location ***./Datasets/PSSM Profiles***.
* ***./Scripts/Pre-Process/DST.py*** applies ***2D-DST*** to each PSSM profile. Updated PSSM Profiles has been added in this location ***./Datasets/DST_Applied***.

***[Less Important]***
* ***split_dataset.py*** script splits the dataset into multiple batches.
* ***remove_UniProt.py*** script removes the 'UniProt' text from the UniProt identifier of each protein. 
* ***replace_tick.py*** script replaces the tick mark (&#10004;).
* ***merge_batches.py*** script merges the batch files.

## Packages Used:
![biopython](https://img.shields.io/badge/Biopython-1.81-green) ![networkx](https://img.shields.io/badge/NetworkX-3.1-yellow) ![pandas](https://img.shields.io/badge/Pandas-2.0.3-blue) ![numpy](https://img.shields.io/badge/Numpy-1.25.0-blue) ![scipy](https://img.shields.io/badge/Scipy-1.11.2-blue) ![pyarrow](https://img.shields.io/badge/Pyarrow-13.0.0-blue)
