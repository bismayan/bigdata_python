# stream.py
from math import cos, sin

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

p = figure(x_range=(-1.1, 1.1), y_range=(-1.1, 1.1))
p.circle(x=0, y=0, radius=1, fill_color='firebrick', line_width=2)

# this is the data source we will stream to
source = ColumnDataSource(data=dict(x=[1], y=[0]))
p.circle(x='x', y='y', size=12, fill_color='cyan', source=source)

def update():
    x, y = source.data['x'][-1], source.data['y'][-1]

    # construct the new values for all columns, and pass to stream
    new_data = dict(x=[x*cos(0.1) - y*sin(0.1)], y=[x*sin(0.1) + y*cos(0.1)])
    source.stream(new_data, rollover=8)

curdoc().add_periodic_callback(update, 150)
curdoc().add_root(p)