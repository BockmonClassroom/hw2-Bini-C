# Author: Bini Chandra
# Date: 01/22/2025
# This python file reads in the PlantLeavesDataset.csv data set and visualizes it using histograms, boxplots, and scatter plots.

# Importing necessary libraries
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read the dataset
data = pd.read_csv("./data/PlantLeavesDataset.csv")

columns = ["Leaf_Length(Cm)", "Leaf_Width(Cm)"]

# Group the data by PlantName
groups = data.groupby("PlantName")

# Helper function to create histograms
def helper(tickLabel, i, binData, column, binColor):
    axes[i].hist(binData, bins=10, alpha=0.7, color=binColor, edgecolor="black")
    axes[i].set_title(tickLabel)
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Count')

# Histograms for each plant type
for column in columns:
    fig, axes = plt.subplots(1, len(groups) + 1, figsize=(15,5)) # Suplots for All + individual groups

    # Plot "All" data
    helper("All", 0, data[column], column, 'pink')

    # Plot each group
    for i, (name, group) in enumerate(groups, start=1):
        helper(name, i, group[column], column, 'lightgreen')


# Boxplots for leaf length and width by plant type
fig, axes = plt.subplots(1, 2, figsize=(15,7))

for ax, column in zip(axes, columns):
    data.boxplot(column=column, by="PlantName", ax=ax)
    data[column].plot.box(ax=ax, positions=[-1], widths=0.5, color='pink') # Add "All" boxplot which is all data combined
    ax.set_title(f"Boxplot of {column} by Plant Type")
    ax.set_xticklabels(list(data["PlantName"].unique()) + ["All"], rotation=25) # ASet x-labels including "All"
    ax.set_xlabel(" ") # Removes default xlabel
    ax.set_ylabel(column)
    ax.grid()
plt.show()


# Scatter plot and regression lines for each plant type
for name, group in groups:
    #name = name of plant
    #group = all data belonging to that individual plant type
    x = group["Leaf_Length(Cm)"]
    y = group["Leaf_Width(Cm)"]

    # Scatter plot for each plant type
    plt.scatter(x,y, label=name, alpha=0.7)

    # Calculate and add regression line
    slope, intercept, r_value, p_value, std_error = stats.linregress(x, y)
    plt.plot(x, intercept + slope * x, 'r') # Line plot
    plt.xlabel("Leaf Length (cm)")
    plt.ylabel("Leaf Width (cm)")
    plt.title("Scatter Plot with Regression Lines")
    plt.legend()
    plt.grid()

plt.show()