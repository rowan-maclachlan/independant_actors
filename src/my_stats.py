"""
A module to collect statistical information about
values of population for a surface.  By calling
the get_stats method a dictionary full of these
values is returned.
This module also contains functionality for producing
scatter plots with this data from module plotly.
"""
import Surface
import Actor as ac
#import statistics as st

def get_stats(surface):
    """
    Retrieve statistics about the Surface and the
    Cellular population.
    :param surface: The surface of a simulation
    :type surface: Surface
    :return: A dictionary full of statistics
    :rtype: dict(str, float)
    """
    stats = dict()
   
    return stats
    
def output_plot(path, data):
    from plotly import offline as py
    from plotly import graph_objs as go

    plot_data = {}
    for key in data[0].keys():
        plot_data[key] = {
            'x': [],
            'y': [],
            'mode': 'lines+markers',
            'name': key
        }

    for i, d in enumerate(data):
        for k, v in d.items():
            plot_data[k]['x'].append(i)
            plot_data[k]['y'].append(v)

    to_plot = []
    for k in sorted(plot_data.keys()):
        to_plot.append(go.Scatter(plot_data[k]))

    py.plot(to_plot, filename=path, auto_open=False)

