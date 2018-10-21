import pandas as pd
import seaborn as sns

data = pd.read_csv('data/mao_b.csv')

# data.groupby(['time', 'concentration']).describe()
# data['abs_c'] = 0

data.loc[data.concentration == 5, 'abc_c'] = 0.2
data.loc[data.concentration == 5, 'abc_c'] = 0.2
data.loc[data.concentration == 2.5, 'abc_c'] = 0.1
data.loc[data.concentration == 1.25, 'abc_c'] = 0.05
data.loc[data.concentration == 0.625, 'abc_c'] = 0.025
