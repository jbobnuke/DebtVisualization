import numpy as np
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(x=x, y=y, line_shape='spline'))
fig.show()