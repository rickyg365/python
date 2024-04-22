import matplotlib.pyplot as plt
import numpy as np

from radar_star import radar_factory

"""
data = [
    ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3'],
    ('Basecase', [
        [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00],
        [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00],
        [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00],
        [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00],
        [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00]]),
    ('With CO', [
        [0.88, 0.02, 0.02, 0.02, 0.00, 0.05, 0.00, 0.05, 0.00],
        [0.08, 0.94, 0.04, 0.02, 0.00, 0.01, 0.12, 0.04, 0.00],
        [0.01, 0.01, 0.79, 0.10, 0.00, 0.05, 0.00, 0.31, 0.00],
        [0.00, 0.02, 0.03, 0.38, 0.31, 0.31, 0.00, 0.59, 0.00],
        [0.02, 0.02, 0.11, 0.47, 0.69, 0.58, 0.88, 0.00, 0.00]]),
    ('With O3', [
        [0.89, 0.01, 0.07, 0.00, 0.00, 0.05, 0.00, 0.00, 0.03],
        [0.07, 0.95, 0.05, 0.04, 0.00, 0.02, 0.12, 0.00, 0.00],
        [0.01, 0.02, 0.86, 0.27, 0.16, 0.19, 0.00, 0.00, 0.00],
        [0.01, 0.03, 0.00, 0.32, 0.29, 0.27, 0.00, 0.00, 0.95],
        [0.02, 0.00, 0.03, 0.37, 0.56, 0.47, 0.87, 0.00, 0.00]]),
    ('CO & O3', [
        [0.87, 0.01, 0.08, 0.00, 0.00, 0.04, 0.00, 0.00, 0.01],
        [0.09, 0.95, 0.02, 0.03, 0.00, 0.01, 0.13, 0.06, 0.00],
        [0.01, 0.02, 0.71, 0.24, 0.13, 0.16, 0.00, 0.50, 0.00],
        [0.01, 0.03, 0.00, 0.28, 0.24, 0.23, 0.00, 0.44, 0.88],
        [0.02, 0.00, 0.18, 0.45, 0.64, 0.55, 0.86, 0.00, 0.16]])
]

"""

def example_data():
    """
    [
        [List of attributes],
        (case_name, data{num of data points == num attributes})
    ]
    """
    def normalize(value: float, normal_factor: float=10.0):
        MAX_ATTR_VAL = 1000.0
        ratio = value/MAX_ATTR_VAL
        
        return ratio * normal_factor

    data = [
        ['HP', 'ATK', 'Sp. ATK', 'SPD', 'Sp. DEF', 'DEF'],
        ('Basecase', [
            [7.00/10, 2.00/10, 0.00/10, 0.00/10, 0.00/10, 2.00/10],
            [2.00/10, 6.00/10, 2.00/10, 0.00/10, 0.00/10, 0.00/10],
            [0.00/10, 2.00/10, 5.00/10, 2.00/10, 0.00/10, 0.00/10],
            [0.00/10, 0.00/10, 2.00/10, 6.00/10, 2.00/10, 0.00/10],
            [0.00/10, 0.00/10, 0.00/10, 2.00/10, 5.00/10, 2.00/10],
            [2.00/10, 0.00/10, 0.00/10, 0.00/10, 2.00/10, 5.00/10]])
    ]

    return data


HP_COLOR = 'b'
ATK_COLOR = 'r'
SPATK_COLOR = 'r'
SPD_COLOR = '#2f2f2f'
SPDEF_COLOR = 'g'
DEF_COLOR = 'y'

if __name__ == '__main__':
    data = example_data()
    N = len(data[0])
    theta = radar_factory(N, frame='polygon')

    spoke_labels = data.pop(0)

    fig, axs = plt.subplots(figsize=(9, 9), nrows=1, ncols=1,
                            subplot_kw=dict(projection='radar'))
    # fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = [ HP_COLOR, ATK_COLOR, SPATK_COLOR, SPD_COLOR, SPDEF_COLOR, DEF_COLOR]
    # Plot the four cases from the example data on separate axes
    # ax = axs[0]
    for (title, case_data) in data:
        axs.set_rgrids([i/10 for i in range(10)])
        axs.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        # For each set of data
        for d, color in zip(case_data, colors):
            axs.plot(theta, d, color=color)
            axs.fill(theta, d, facecolor=color, alpha=0.25, label='_nolegend_')

    # Plot the four cases from the example data on separate axes
    # for ax, (title, case_data) in zip(axs.flat, data):
    #     ax.set_rgrids([i/10 for i in range(10)])
    #     ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
    #                  horizontalalignment='center', verticalalignment='center')
    #     # For each set of data
    #     for d, color in zip(case_data, colors):
    #         ax.plot(theta, d, color=color)
    #         ax.fill(theta, d, facecolor=color, alpha=0.25, label='_nolegend_')

        axs.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
    labels = (l for l in spoke_labels)
    
    # multiple subplots
    # legend = axs[0, 0].legend(labels, loc=(0.9, .95),
    #                           labelspacing=0.1, fontsize='small')

    # Single
    legend = axs.legend(labels, loc=(0.9, .95),
                              labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, 'Some bullshit title',
             horizontalalignment='center', color='black', weight='bold',
             size='large')

    plt.show()