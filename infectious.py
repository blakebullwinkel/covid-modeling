import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

coronavirus_data = pd.read_excel('coronavirus.xlsx', sheet_name='全国')
coronavirus_data['day'] = coronavirus_data['Date'].dt.strftime('%b %d')

fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
cases = sns.barplot(x='day', y='Infections', data=coronavirus_data, color=(1.0, 0.2471, 0.2471))
cases.set_xticklabels(cases.get_xticklabels(), rotation=90)
ax.set_ylabel('')
ax.set_xlabel('')

plt.show()
