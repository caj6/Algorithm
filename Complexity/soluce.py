import os
import pandas as pd
from collections import defaultdict

def pairs(csv_files, target):
    seen_values = set();  # Set to store already-seen values
    pairs_found = [];  # List that stores pairs that match the target sum
    
    # all CSV files into a single list
    all_values = [];
    for csv_file in csv_files:
        data = pd.read_csv(csv_file);
        num_list = data['Value'].tolist();
        all_values.extend(num_list);
    
    # look for pairs that form the target sum
    for val in all_values:
        complement = target - val;
        if complement in seen_values:
            pairs_found.append((val, complement));
        seen_values.add(val);
    return pairs_found;

# loading csv files from their folder
folder_path = r'C:\Users\junio\OneDrive\Documents\CESI\A3\Algo\Algo4\JeremyData'; 
csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')];

# Get target sum from the user
target = int(input("Enter the target : "))  
matching = pairs(csv_files, target);

# Print the pair(s) 
if matching:
    print(f"Pairs that sum to {target}: {matching}");
else:
    print(f"No pairs found that sum to {target}.");

