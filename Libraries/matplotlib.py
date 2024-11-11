import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample Data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_cos = np.cos(x)

# 1. Line Plot
# ------------
print("1. Line Plot")
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine', color='b', linestyle='-', linewidth=2)
plt.plot(x, y_cos, label='Cosine', color='r', linestyle='--', linewidth=2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot of Sine and Cosine Functions")
plt.legend()
plt.grid(True)
plt.show()


# 2. Scatter Plot
# ---------------
print("2. Scatter Plot")
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.figure(figsize=(8, 4))
plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Random Points")
plt.colorbar()  # Show color scale
plt.show()


# 3. Bar Plot
# -----------
print("3. Bar Plot")
categories = ['Category A', 'Category B', 'Category C']
values = [7, 3, 5]

plt.figure(figsize=(8, 4))
plt.bar(categories, values, color=['blue', 'green', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot of Categories")
plt.show()


# 4. Horizontal Bar Plot
# ----------------------
print("4. Horizontal Bar Plot")
plt.figure(figsize=(8, 4))
plt.barh(categories, values, color=['blue', 'green', 'purple'])
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Plot of Categories")
plt.show()


# 5. Histogram
# ------------
print("5. Histogram")
data = np.random.randn(1000)

plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, color='c', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Data")
plt.show()


# 6. Box Plot
# -----------
print("6. Box Plot")
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure(figsize=(8, 4))
plt.boxplot(data_box, vert=True, patch_artist=True, labels=['std=1', 'std=2', 'std=3'])
plt.xlabel("Distribution")
plt.ylabel("Value")
plt.title("Box Plot of Different Standard Deviations")
plt.show()


# 7. Pie Chart
# ------------
print("7. Pie Chart")
sizes = [20, 30, 25, 25]
labels = ['Section A', 'Section B', 'Section C', 'Section D']
explode = (0.1, 0, 0, 0)  # explode the 1st slice

plt.figure(figsize=(8, 4))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart Example")
plt.show()


# 8. Subplots
# -----------
print("8. Subplots")
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
axs[0, 0].plot(x, y, 'b-')
axs[0, 0].set_title('Sine Wave')

# Scatter plot
axs[0, 1].scatter(x_scatter, y_scatter, c=colors, s=100, alpha=0.5, cmap='viridis')
axs[0, 1].set_title('Scatter Plot')

# Bar plot
axs[1, 0].bar(categories, values, color=['blue', 'green', 'purple'])
axs[1, 0].set_title('Bar Plot')

# Histogram
axs[1, 1].hist(data, bins=30, color='c', edgecolor='black')
axs[1, 1].set_title('Histogram')

# Layout adjustment
plt.tight_layout()
plt.show()


# 9. 3D Plot
# ----------
print("9. 3D Plot")
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
ax.plot(x, y, z, label='3D Line Plot', color='m')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.legend()
plt.show()


# 10. Heatmap
# -----------
print("10. Heatmap")
data_heatmap = np.random.rand(10, 10)

plt.figure(figsize=(8, 6))
plt.imshow(data_heatmap, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap Example")
plt.show()


# 11. Time Series Plot
# --------------------
print("11. Time Series Plot")
dates = pd.date_range(start='2023-01-01', periods=100)
time_series_data = pd.Series(np.random.randn(100).cumsum(), index=dates)

plt.figure(figsize=(10, 5))
time_series_data.plot(color='b')
plt.title("Time Series Plot")
plt.xlabel("Date")
plt.ylabel("Cumulative Sum")
plt.grid(True)
plt.show()


# 12. Annotations
# ---------------
print("12. Annotations")
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine', color='b')
plt.plot(x, y_cos, label='Cosine', color='r')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot with Annotations")
plt.legend()

# Adding annotation
plt.annotate('Max Sine', xy=(1.5 * np.pi, 1), xytext=(5, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
