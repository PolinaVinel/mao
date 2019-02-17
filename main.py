import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

data = pd.read_csv('data/mao_b_r.csv')


data.concentration.describe()


# data.loc[data.concentration == 7.5, 'abc_c'] = 0.3
# data.loc[data.concentration == 3.75, 'abc_c'] = 0.15
# data.loc[data.concentration == 1.86, 'abc_c'] = 0.07
# data.loc[data.concentration == 0.93, 'abc_c'] = 0.037
#
# data['D'] = data.value / (data.time * data.abc_c)
#
# # save data
# data.to_csv('data/mao_b_r.csv', index=False)

def show_concentration_plot(data, title):
    fig, ax = plt.subplots()
    # sns.swarmplot(x='concentration', y='D', data=data, edgecolor="black", linewidth=.9, ax=ax)
    sns.boxplot(x='concentration', y='value', data=data, saturation=1, ax=ax)
    sns.pointplot(x='concentration', y='value', data=data, linestyles='--', scale=0.4,
                  color='k', errwidth=0, capsize=0, ax=ax)
    plt.ylabel("value")
    plt.title(title)

    # plt.ylim(0, 0.8)
    plt.savefig('plot/concentration_plot.svg', format='svg')
    plt.show()


def show_d_plot(data, title):
    fig, ax = plt.subplots()
    # sns.swarmplot(x='concentration', y='D', data=data, edgecolor="black", linewidth=.9, ax=ax)
    sns.boxplot(x='concentration', y='value', data=data, saturation=1, ax=ax)
    sns.pointplot(x='concentration', y='value', data=data, linestyles='--', scale=0.4,
                  color='k', errwidth=0, capsize=0, ax=ax)
    plt.ylabel("D")
    plt.title(title)

    # plt.ylim(0, 0.8)
    plt.savefig('plot/d_plot.svg', format='svg')
    plt.show()


def show_time_plot(data, title):
    fig, ax = plt.subplots()
    # sns.swarmplot(x='time', y='D', data=data, edgecolor="black", linewidth=.9, ax=ax)
    sns.boxplot(x='time', y='value', data=data, saturation=1, ax=ax)
    sns.pointplot(x='time', y='value', data=data, linestyles='--', scale=0.4,
                  color='k', errwidth=0, capsize=0, ax=ax)
    plt.ylabel("D")
    plt.title(title)

    # plt.ylim(0, 0.8)
    plt.savefig('plot/time_plot.svg', format='svg')
    plt.show()

#show_d_plot(data=data[data.time == 5], title='Время инкубации 5 мин')
#show_d_plot(data=data[data.time == 10], title='Время инкубации 10 мин')
#show_d_plot(data=data[data.time == 15], title='Время инкубации 15 мин')
#show_d_plot(data=data[data.time == 20], title='Время инкубации 20 мин')
#show_time_plot(data=data[data.concentration == 7.5], title='Концентрация белка 7.5 г/л')
#show_time_plot(data=data[data.concentration == 3.75], title='Концентрация белка 3.75 г/л')
#show_time_plot(data=data[data.concentration == 1.86], title='Концентрация белка 1.86 г/л')
#show_time_plot(data=data[data.concentration == 0.93], title='Концентрация белка 0,93 г/л')
#show_concentration_plot(data=data, title='Время,мин')
#show_time_plot(data=data, title='Концентрация,г/л')

data[(data.time == 15.0) & (data.concentration == 7.5)].value.describe()

import pandas as pd
import seaborn as sns

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0.15, .21, .39, .45, .51, .68, .74, .86, .98, 1.0]
import matplotlib.pyplot as plt
import numpy as np


#data = pd.read_csv('data/mao_b_r.csv')
#d = data[data.time == 20]
#t = d.groupby('concentration').value.mean()


#x = np.array(t.index) data.
#y = np.array(t.values)

max = 0
i_max = 0
for i in range(0, len(x) - 1):
    t = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    if t > max:
        max = t
        i_max = i

print(max)
print('x1 = ', x[i_max])
print('x2 = ', x[i_max + 1])
print('y1 = ', y[i_max])
print('y2 = ', y[i_max + 1])

sns.lineplot(x, y)
sns.lineplot([x[i_max], x[i_max + 1]], [y[i_max], y[i_max + 1]])
plt.show()