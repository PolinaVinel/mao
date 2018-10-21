import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

data = pd.read_csv('data/mao_b.csv')


# data.groupby(['time', 'concentration']).describe()
# data['abs_c'] = 0

# data.loc[data.concentration == 5, 'abc_c'] = 0.2
# data.loc[data.concentration == 5, 'abc_c'] = 0.2
# data.loc[data.concentration == 2.5, 'abc_c'] = 0.1
# data.loc[data.concentration == 1.25, 'abc_c'] = 0.05
# data.loc[data.concentration == 0.625, 'abc_c'] = 0.025
#
# data['D'] = data.value / (data.time * data.abc_c)

# save data
# data.to_csv('data/mao_b.csv', index=False)

def show_plot(data, title):
    fig, ax = plt.subplots()
    # sns.swarmplot(x='concentration', y='D', data=data, edgecolor="black", linewidth=.9, ax=ax)
    sns.boxplot(x='concentration', y='D', data=data, saturation=1, ax=ax)
    sns.pointplot(x='concentration', y='D', data=data, linestyles='--', scale=0.4,
                  color='k', errwidth=0, capsize=0, ax=ax)
    plt.ylabel("D")
    plt.title(title)

    plt.show()


# show_plot(data=data[data.time == 5], title='Time 5 min')
show_plot(data=data[data.time == 10], title='Time 10 min')
