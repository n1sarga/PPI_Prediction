import os
import pandas as pd
import networkx as nx
import itertools

# Directory containing all batch files
directory = "D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Maize_Split"

# Directory to save positive-negative interaction files
output_directory = "D:\\Profiles\\Nisarga Mridha\\Study\\CSE400A\\Datasets\\Maize\\Positive_Negative_Interactions"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        
        # Read Dataset
        df = pd.read_csv(filepath)

        positive_interactions = df[df['Interaction'] == 1]
        G = nx.Graph()
        G.add_edges_from(positive_interactions[['Identifier A', 'Identifier B']].values)

        all_nodes = set(df['Identifier A']).union(set(df['Identifier B']))
        all_edges = set(itertools.combinations(all_nodes, 2))
        negative_interactions = all_edges - set(G.edges)

        # Randomly sample 500 negative interactions
        negative_df = pd.DataFrame(list(negative_interactions), columns=['Identifier A', 'Identifier B'])
        negative_df['Interaction'] = 0
        sampled_negative_df = negative_df.sample(n=500, random_state=42)

        # Combine positive interactions and sampled negative interactions
        all_interactions = pd.concat([positive_interactions, sampled_negative_df])

        # Save to CSV
        output_filepath = os.path.join(output_directory, filename)
        all_interactions.to_csv(output_filepath, index=False)
