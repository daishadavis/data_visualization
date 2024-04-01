import matplotlib.pyplot as plt

#Data
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

#Plot
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axis.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value")

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

#Set the range for each axis.
ax.axis([0, 5000, 0, 125000000000])

plt.show()