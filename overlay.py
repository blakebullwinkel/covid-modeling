import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

coronavirus_data = pd.read_excel('coronavirus.xlsx', sheet_name='全国')
coronavirus_data['day'] = coronavirus_data['Date'].dt.strftime('%b %d')

fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
cases = sns.barplot(x='day', y='Cum Cases', data=coronavirus_data, color='dodgerblue')
sns.barplot(x='day', y='Cum Recoveries', data=coronavirus_data, color=(0.0, 0.6902, 0.3137))
sns.barplot(x='day', y='Cum Deaths', data=coronavirus_data, color=(1.0, 0.2471, 0.2471))
cases.set_xticklabels(cases.get_xticklabels(), rotation=90)
ax.set_ylabel('Number of people')
ax.set_xlabel('')

legend_elements = [Line2D([0], [0], marker='o', color='w', label='Total Cases',
                          markerfacecolor='dodgerblue', markersize=10),
                    Line2D([0], [0], marker='o', color='w', label='Recoveries',
                          markerfacecolor=(0.0, 0.6902, 0.3137), markersize=10),
                    Line2D([0], [0], marker='o', color='w', label='Deaths',
                          markerfacecolor=(1.0, 0.2471, 0.2471), markersize=10)]

ax.legend(handles=legend_elements, loc='upper left')

#fig.legend(labels=['Total Cases', 'Recoveries', 'Deaths'], loc='upper left', bbox_to_anchor=(0.13, 0.875))

plt.show()
