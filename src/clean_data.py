import pandas as pd
import numpy as np
from pandas import isnull
from src.data_loader import species_info_raw, observations_raw

species_observations_raw = pd.merge(species_info_raw, observations_raw, how = 'left', on = 'scientific_name')

print(species_observations_raw.columns)

# We can assume that any species with nan in conservation_status implies that they are not endangered.
species_observations_raw['conservation_status'] = species_observations_raw['conservation_status'].replace( np.nan, 'Not Endangered')

species_observations = species_observations_raw


