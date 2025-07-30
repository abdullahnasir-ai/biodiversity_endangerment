from src.clean_data import species_observations
import matplotlib.pyplot as plt

print('Species by Conservation status:')
print(species_observations['conservation_status'].value_counts())


