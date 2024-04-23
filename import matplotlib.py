import matplotlib.pyplot as plt

# Data
labels = ['Sand', 'Silt', 'Clay', 'Organic Matter']
sizes = [40, 30, 20, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.1, 0, 0, 0)  # explode the 1st slice (Sand)

# Plot
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Soil Composition')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()