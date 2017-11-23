import numpy as np

import matplotlib.pyplot as plt

import matplotlib as mpl


def draw_pie(labels, quants):
    # make a square figure

    plt.figure(1, figsize=(6, 6))

    # For China, make the piece explode a bit

    expl = [0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0]

    # Colors used. Recycle if not enough.

    colors = ["blue", "red", "coral", "green", "yellow", "orange"]

    # Pie Plot

    # autopct: format of "percent" string;

    plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8, shadow=True)

    plt.title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})

    plt.show()


def draw_bar(labels, quants):
    width = 0.4

    ind = np.linspace(0.5, 9.5, 10)

    # make a square figure

    fig = plt.figure(1)

    ax = fig.add_subplot(111)

    # Bar Plot

    ax.bar(ind - width / 2, quants, width, color='green')

    # Set the ticks on x-axis

    ax.set_xticks(ind)

    ax.set_xticklabels(labels)

    # labels

    ax.set_xlabel('Country')

    ax.set_ylabel('GDP (Billion US dollar)')

    # title

    ax.set_title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})

    plt.grid(True)

    plt.show()


def draw_line(labels, quants):
    ind = np.linspace(0, 9, 10)

    fig = plt.figure(1)

    ax = fig.add_subplot(111)

    ax.plot(ind, quants)

    ax.set_title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})

    ax.set_xticklabels(labels)

    plt.grid(True)

    plt.show()


# quants: GDP

# labels: country name

labels = ['USA', 'China', 'India', 'Japan', 'Germany', 'Russia', 'Brazil', 'UK', 'France', 'Italy']

quants = [15094025.0, 11299967.0, 4457784.0, 4440376.0, 3099080.0, 2383402.0, 2293954.0, 2260803.0, 2217900.0,
          1846950.0]

#draw_pie(labels, quants)

draw_bar(labels,quants)

# draw_line(labels,quants)