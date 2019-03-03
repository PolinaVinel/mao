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

#10 мин7,5
x = [5, 10, 15, 20, 25, 30, 35]
#y = [2.2267, 2.2190, 2.2139, 2.1312, 2.0939, 2.0596]
#3,75
#x = [5, 10, 15, 20, 25, 30]
#y = [1.2090, 1.2019, 1.2021, 1.1983, 1.1966, 1.1933]
#1,86
#y = [0.6827, 0.6824, 0.6806, 0.6791, 0.6816, 0.6776]
#0,93
#y = [0.3504, 0.3498, 0.3479, 0.3527, 0.3476, 0.3478]

#15мин7,5
#y = [2.3785, 2.2314, 2.1899, 2.1466, 2.1056, 2.0462, 2.0366]

#3,75
#y = [1.1821, 1.1725, 1.1670, 1.1631, 1.1636, 1.1505, 1.1534]

#1,86
#y = [0.6671, 0.6664, 0.6680, 0.6660, 0.6624, 0.6652, 0.6683]

#0,93
#y = [0.3746, 0.3763, 0.3745, 0.3742, 0.3755, 0.3736, 0.3761]

#25мин 7,5
#y = [2.0260, 2.0344, 2.0358, 2.0369, 2.0435, 2.0306]
#3,75
#y = [1.0828, 1.0784, 1.08, 1.0775, 1.0731, 1.0743, 1.0665]
#1,86
#y = [0.6578, 0.6611, 0.6590, 0.6582, 0.6544, 0.6536, 0.6536]
#0,93
#y = [0.3993, 0.4025, 0.3974, 0.3988, 0.3980, 0.3961, 0.3979]

#30мин 7,5
#y = [2.0725, 2.0523, 2.0458, 2.0273, 2.0608, 2.0231, 2.0128]
#3,5
#y = [1.1589, 1.1561, 1.1558, 1.1520, 1.1572, 1.1502, 1.1487]
#1,86
#y = [0.6165, 0.6152, 0.6137, 0.6120, 0.6132, 0.6101, 0.6105]
#0,93
y = [0.3587, 0.3593, 0.3567, 0.3584, 0.3577, 0.3546, 0.3543]

import matplotlib.pyplot as plt
import numpy as np


#data = pd.read_csv('data/mao_b_r.csv')
#d = data[data.time == 20]
#t = d.groupby('concentration').value.mean()


#x = np.array(t.index) data.
#y = np.array(t.values)
import math
max = 0
i_max = 0
for i in range(0, len(x) - 1):
    t = math.fabs((y[i + 1] - y[i])/ (x[i + 1] - x[i]))
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
plt.ylabel("D")
plt.xlabel("t,min")


plt.title("40 минут инубации с ДНФГ, 0,93 г/л")
plt.show()

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import numpy as np
x = [5, 10, 15, 20, 25, 30, 35]
y = [2.2267, 2.2190, 2.2139, 2.1312, 2.0939, 2.0596]
sns.lineplot(x, y)

y = [1.2090, 1.2019, 1.2021, 1.1983, 1.1966, 1.1933]
sns.lineplot(x, y)

y = [0.6827, 0.6824, 0.6806, 0.6791, 0.6816, 0.6776]
sns.lineplot(x, y)

y = [0.3504, 0.3498, 0.3479, 0.3527, 0.3476, 0.3478]
sns.lineplot(x, y)

plt.ylabel("D")
plt.xlabel("t,min")


plt.title("40 минут инубации с ДНФГ, 0,93 г/л")
plt.show()
