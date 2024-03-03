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