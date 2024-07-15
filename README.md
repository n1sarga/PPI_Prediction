# PPI_Prediction_Maize

## Dataset Description
* Plant Name: ***Zea mays (Maize)***
* Dataset Size: ***101,869 &times; 3***
* Online Repository: ***IntAct***
* Interaction Types: ***Positive and Negative Interactions***
* ***PSSM Profiles*** in ***parquet*** format has been added.

## Script Description
***[Important]***
* ***seq.py*** script collects protein sequences against each UniProt Protein Identifier using ***UniProt REST-API***.
* ***bipartite_graph.py*** script generates the non-interacting protein combination from positive interactions.
* ***./Scripts/Pre-Process/PSSM.py*** generates the PSSM profiles against each protein sequence.
* ***./Scripts/Pre-Process/DST.py*** applies ***2D-DST*** to each PSSM profile.

***[Less Important]***
* ***split_dataset.py*** script splits the dataset into multiple batches.
* ***remove_UniProt.py*** script removes the 'UniProt' text from the UniProt identifier of each protein. 
* ***replace_tick.py*** script replaces the tick mark (&#10004;).
* ***merge_batches.py*** script merges the batch files.
