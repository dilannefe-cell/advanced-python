from fingers_erp import calc_mean_erp

# File paths
trial_points_file = 'events_file_ordered.csv'
ecog_data_file = 'brain_data_channel_one.csv'

# Call the function
fingers_erp_mean = calc_mean_erp(trial_points_file, ecog_data_file)

# Print the shape to verify it's correct
print(f"Shape of result: {fingers_erp_mean.shape}")
print(f"Expected shape: (5, 1201)")

# Print some statistics
print("\nMean values for each finger:")
for i in range(5):
    print(f"Finger {i+1}: {fingers_erp_mean[i, :].mean():.2f}")
