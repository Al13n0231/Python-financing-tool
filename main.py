# ******************************
# @TODO: calculate the standard deviation of y, and plot it on a new plot
# ******************************


import pandas as pd
import matplotlib.pyplot as plt

# ************* LOAD DATAFRAME FROM CSV *****************

# Function to load data from a CSV file
def load_data(file_path):
    try:
        # @TODO read the docs for read_csv
        df = pd.read_csv(file_path, names=["x", "y"], header=3)
        print(df)
        return df
    except FileNotFoundError:
        print(f"The file at {file_path} was not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

# Load the data from both files
location_of_data = "C:\\Users\\Lenovo\\Projects\\Python-financing-tool\\sample.csv"
df = load_data(location_of_data)

# ************* PLOT DATAFRAME *****************

print(df['y'])

# create plot
# @TODO google matplotlib
plt.plot(df['x'], df['y'], marker='o', linestyle='-')
# matplotlib is a library for creating static, animated, and interactive visualizations in Python.
# I found the 3D surface to be very interesting, instead of making data like:
# X = ... Y=... Z=... They use meshgrid to explain the array values from Numpy
# @ graphing a 3D surface with matplotlib
import numpy as np
from matplotlib import cm

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)


ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
# @NOTE all of these things below help make our chart "pretty" and are not necessary
# plt.title('Square Sine Wave')

# plt.xlabel('X')

# plt.ylabel('Y')

# rotates the x axis text
# plt.xticks(rotation=45)

# displays a grid on the chart
# plt.grid(True)

# some kind of custom layout? 
# plt.tight_layout()

plt.show()

#@ calculate the standard deviation of y, and plot it on a new plot
import statistics
import seaborn as sns

sns.set_style('darkgrid')
#matplotlib inline
sns.mpl.rcParams['figure.figsize'] = (10.0, 8.0)

print(statistics.stdev([132.44 , 200.00, 4200.00, 3.00, 34.00, 54.00]))
df = pd.read_csv('C:\\Users\\Lenovo\\Projects\\Python-financing-tool\\sample.csv')
print(df.columns)
df.columns = ['year', 'value']
std_dev = df['value'].std()

# Create a scatter plot
sns.set(style="darkgrid")
plt.figure(figsize=(10, 8))
graph = sns.scatterplot(x=df['year'], y=df['value'])

# Add a horizontal line for the standard deviation
graph.axhline(y=std_dev, color='red', linestyle='--')

# Add labels and title if needed
plt.title('Scatter plot with Standard Deviation')
plt.xlabel('year')
plt.ylabel('value')

# Show the plot
plt.show()
