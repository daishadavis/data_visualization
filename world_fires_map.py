import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lons = []
    lats = []
    brightnesses = []

    for row in reader:
        lon = float(row[1])
        lat = float(row[0])
        brightness = float(row[2])
        lons.append(lon)
        lats.append(lat)
        brightnesses.append(brightness)

    # Map the fires
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [5*brightness for brightness in brightnesses],
            'color': brightnesses,
            'colorscale': 'Hot',
            'reversescale': True,
            'colorbar': {'title': 'Brightness'}
        }
    }]

    my_layout = Layout(title='Global Fires')

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_fires.html')
