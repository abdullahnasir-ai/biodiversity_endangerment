from src.clean_data import species_observations
import matplotlib.pyplot as plt

print(species_observations['conservation_status'].value_counts())

percentage_of_endangered = len(species_observations[species_observations['conservation_status'] == 'Endangered']) / len(species_observations)
print(f'Percentage of Endangered Observations: {percentage_of_endangered:.4f}%')
# Endangered Observations account for 0.0031% of the dataset

