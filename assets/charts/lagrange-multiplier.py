import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

x, l = np.linspace(-1, 1, 10), np.linspace(-1, 1, 10)
x, l = np.meshgrid(x, l)
z = x * x + x * l

fig = go.Figure(data=[go.Surface(z=z, x=x, y=l)])

fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))

fig.update_layout(
    title='L(x, lambda)= x^2 + lambda * x',
    scene = dict(
        xaxis_title='x',
        yaxis_title='lambda',
        zaxis_title='L'),
        width=500, height=500,
        margin=dict(l=65, r=50, b=65, t=90))

fig.show()

pio.write_html(fig, file='_includes/charts/lagrange-multiplier.html', auto_open=True)
