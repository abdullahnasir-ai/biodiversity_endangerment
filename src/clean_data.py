import pandas as pd
from src.data_loader import species_info_raw, observations_raw

species_observations_raw = pd.merge(species_info_raw, observations_raw, how = 'left', on = 'scientific_name')
