import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/Users/daishadavis/Documents/data_visualization/data/san_francisco_highs_lows_2013-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from file.
    dates, highs,lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = int(row[7])
        low = int(row[8])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format
    plt.title("Daily high low temperatures 2013-2014\n San Francisco, CA", fontsize=20)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)

    plt.savefig('san_francisco_highs_lows_png', bbox_inches='tight')

        