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
    sns.boxplot(x='concentration', y='D', data=data, saturation=1, ax=ax)
    sns.pointplot(x='concentration', y='D', data=data, linestyles='--', scale=0.4,
                  color='k', errwidth=0, capsize=0, ax=ax)
    plt.ylabel("D")
    plt.title(title)

    # plt.ylim(0, 0.8)
    plt.savefig('plot/d_plot.svg', format='svg')
    plt.show()


def show_time_plot(data, title):
    fig, ax = plt.subplots()
    # sns.swarmplot(x='time', y='D', data=data, edgecolor="black", linewidth=.9, ax=ax)
    sns.boxplot(x='time', y='D', data=data, saturation=1, ax=ax)
    sns.pointplot(x='time', y='D', data=data, linestyles='--', scale=0.4,
                  color='k', errwidth=0, capsize=0, ax=ax)
    plt.ylabel("D")
    plt.title(title)

    # plt.ylim(0, 0.8)
    plt.savefig('plot/time_plot.svg', format='svg')
    plt.show()


# show_d_plot(data=data[data.time == 15], title='Time 15 min')
# show_d_plot(data=data[data.time == 20], title='Time 20 min')
show_time_plot(data=data[data.concentration == 7.5], title='Concentration 7.5')
show_time_plot(data=data[data.concentration == 3.75], title='Concentration 3.75')
show_time_plot(data=data[data.concentration == 1.86], title='Concentration 1.86')
show_time_plot(data=data[data.concentration == 0.93], title='Concentration 0.93')
# show_concentration_plot(data=data, title='Time')
# show_time_plot(data=data, title='concentration')

data[(data.time == 15.0) & (data.concentration == 7.5)].value.describe()