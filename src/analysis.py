from src.clean_data import species_observations
import matplotlib.pyplot as plt

print('Species by Conservation status:')
print(species_observations['conservation_status'].value_counts())

percentage_of_endangered = (len(species_observations[species_observations['conservation_status'] == 'Endangered']) / len(species_observations)) * 100
print(f'Percentage of Endangered Observations: {percentage_of_endangered:.2f}%')
# Endangered Observations account for 0.31% of the dataset


