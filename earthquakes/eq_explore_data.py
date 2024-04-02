import json

# Explore the structure of the data.

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lags = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lag = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lags.append(lag)

print(mags[:10])
print(lons[:5])
print(lags[:5])