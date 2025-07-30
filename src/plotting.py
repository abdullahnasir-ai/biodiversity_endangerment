import matplotlib.pyplot as plt
from src.clean_data import species_observations
import seaborn as sns
from src.analysis import table1_df, table2_df

plt.figure(figsize = (8,6))
sns.barplot(data = table1_df, x = 'conservation_status', y = 'count')
plt.xticks(rotation = 45)
plt.xlabel('Conservation Status')
plt.ylabel('Number of Observations')
plt.title('Species by Conservation Status')
plt.show()
plt.clf()
plt.savefig('species_by_conservation_status')

