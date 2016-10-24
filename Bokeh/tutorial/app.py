# app.py

from numpy.random import random
import numpy

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.plotting import ColumnDataSource, Figure
from bokeh.models.widgets import Select, TextInput,Slider


Slider_size=Slider(start=0.01,end=0.5, step=0.01,value=0.03,title="scaling size of circles")

def get_data(N):
    return dict(x=random(size=N), y=random(size=N),r=numpy.ones(N)*Slider_size.value)

source = ColumnDataSource(data=get_data(200))
p = Figure()
r = p.circle(x='x', y='y', radius='r', source=source,
             color="navy", alpha=0.6, line_color="white")

COLORS = ["black", "firebrick", "navy", "olive", "goldenrod"]
select = Select(title="Color", value="navy", options=COLORS)
input = TextInput(title="Number of points", value="200")
input_y = TextInput(title="Y-Axis Label", value="Default_y")
input_x = TextInput(title="X-Axis Label", value="Default_x")
Slider_size=Slider(start=0.01,end=0.5, step=0.01,value=0.03,title="scaling size of circles")

Slider_alpha=Slider(start=0.1,end=1.0, step=0.01,value=0.2,title="Transparency of circles")

def update_size(attrname, old, new):
    source.data['r'] = numpy.ones(int(input.value))*Slider_size.value
Slider_size.on_change('value', update_size)


def update_alpha(attrname, old, new):
    r.glyph.fill_alpha = Slider_alpha.value
Slider_alpha.on_change('value', update_alpha)


def update_xaxis(attrname, old, new):
    p.xaxis.axis_label = numpy.array([Slider_size.value]*int(input.value))
input_x.on_change('value', update_xaxis)

def update_yaxis(attrname, old, new):
    p.yaxis.axis_label = input_y.value
input_y.on_change('value', update_yaxis)

def update_color(attrname, old, new):
    r.glyph.fill_color = select.value
select.on_change('value', update_color)

def update_points(attrname, old, new):
    N = int(input.value)
    source.data = get_data(N)
input.on_change('value', update_points)





layout = column(row(select, input,input_x,Slider_size,Slider_alpha,input_y, width=400), row(p),)

curdoc().add_root(layout)

