import pandas as panda
import plotly.express as plots

data = panda.read_csv('data.csv')
f = plots.scatter(data, x = 'date', y = 'cases', size = 'cases', color = "country", size_max = 60)
f.show()
