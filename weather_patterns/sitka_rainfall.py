import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

   # Get dates and daily rainfall from file.
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = (float(row[3]))
        dates.append(current_date)
        rainfall.append(rain)

    # Plot the rainfall
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, rainfall, c='blue')

    # Format Plot
    plt.title("Sitka Rainfall 2018", fontsize=20)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel("Rainfall", fontsize=14)

    plt.savefig('sitka_rainfall.png', bbox_inches='tight')