import pandas as pd

observations_raw = pd.read_csv('/Users/dully/PycharmProjects/biodiversity_endangerment/data/observations.csv')
species_info_raw = pd.read_csv('/Users/dully/PycharmProjects/biodiversity_endangerment/data/species_info.csv')

print(observations_raw.head())
print(species_info_raw.head())

print(observations_raw.info())
print(species_info_raw.info())

print(observations_raw.describe())
print(species_info_raw.describe())


