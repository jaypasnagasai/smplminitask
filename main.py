import numpy as np

# Path to the .npz file
file_path = 'stand.npz'

# Load the .npz file
data = np.load(file_path)

# Print the keys (names of the arrays in the file)
print("Keys in the .npz file:")
print(data.files)

# Print each array and its shape
for key in data.files:
    print(f"\nData for key '{key}':")
    print(data[key])
    print("Shape:", data[key].shape)

# Close the file (optional but good 



# Week 2 Agenda
# Finish the mini task
# Figure out what 156 corresponds to
# Figure out the angles
# Download the entire dataset
# Text Descriptions for each [Human3D]
