from src.clean_data import species_observations
import matplotlib.pyplot as plt

print('Species by Conservation status:')
table1 = species_observations['conservation_status'].value_counts()
table1_df = table1.reset_index()
table1_df.columns = ['conservation_status', 'count']
print(species_observations['conservation_status'].value_counts())

percentage_of_endangered = (len(species_observations[species_observations['conservation_status'] == 'Endangered']) / len(species_observations)) * 100
print(f'Percentage of Endangered Observations: {percentage_of_endangered:.2f}%')
# Endangered Observations account for 0.31% of the dataset

print('Species by Category:')
print(species_observations['category'].value_counts())
table2 = species_observations['category'].value_counts()
table2_df = table2.reset_index()
table2_df.columns = ['category', 'count']

percentage_of_vascular_plant = (len(species_observations[species_observations['category'] == 'Vascular Plant']) / len(species_observations)) * 100
print(f'Percentage of Observations that are Vascular Plants: {percentage_of_vascular_plant:.2f}%')
# Vascular Plants make up 76.31% of the dataset

print(species_observations.columns)

print('Number of Endangered species by category:')
print(species_observations[species_observations['conservation_status'] == 'Endangered'].groupby('category').size())
# Majority of the Endangered observations are those of mammals

print('Number of Endangered observations per National Park:')
print(species_observations[species_observations['conservation_status'] == 'Endangered'].groupby('park_name').size())
# We can see that the number of reports of endangered species across all national parks is the same at 20 each.




