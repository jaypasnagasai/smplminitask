import numpy as np
import pandas as pd

# Load the NPZ file
file_path = 'stand.npz'  # Replace with your file path
data = np.load(file_path)

# Extract the 'poses' data
poses_data = data['poses']

# Define the indices for joint [4]
joint_index = 4
values_per_joint = 3  # Each joint has 3 dimensions (e.g., X, Y, Z)
start_idx = joint_index * values_per_joint
end_idx = start_idx + values_per_joint

# Extract pose data for joint [4]
joint_4_data = poses_data[:, start_idx:end_idx]

# Save the joint 4 data to an NPZ file
output_npz_path = 'joint_4_pose_data.npz'  # Replace with your desired output path
np.savez(output_npz_path, joint_4_poses=joint_4_data)
