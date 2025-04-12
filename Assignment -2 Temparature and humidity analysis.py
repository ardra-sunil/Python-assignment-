import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    'Temperature (°C)': [28, 30, 31, 29, 27, 26, 28],
    'Humidity (%)': [65, 60, 58, 62, 67, 70, 68]
}

df = pd.DataFrame(data)

avg_levels = df.drop('Day', axis=1).mean()
max_levels = df.drop('Day', axis=1).max()
min_levels = df.drop('Day', axis=1).min()

#Line Plot for Temperature & Humidity Over Days ---
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Temperature (°C)'], marker='o', label='Temperature (°C)', color='orange')
plt.plot(df['Day'], df['Humidity (%)'], marker='s', label='Humidity (%)', color='royalblue')
plt.title("Temperature and Humidity Over One Week")
plt.xlabel("Day")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#Bar Plot for Statistical Analysis ---
labels = ['Temperature (°C)', 'Humidity (%)']
x = np.arange(len(labels))  # label locations
width = 0.25  # bar width

fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - width, min_levels, width, label='Min', color='blue')
bars2 = ax.bar(x, avg_levels, width, label='Average', color='lightgreen')
bars3 = ax.bar(x + width, max_levels, width, label='Max', color='red')

ax.set_ylabel('Values')
ax.set_title('Statistical Analysis of Temperature and Humidity')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()
