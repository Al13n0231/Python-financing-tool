# @TODO plot effecient frontier using any datasource on the internet (can also be a .csv file that you download)
import pandas as pd
# Read data from a CSV file
df = pd.read_csv("C:\Users\Lenovo\Downloads\food-price-index-september-2023-index-numbers.csv")

# Display the first few rows of the DataFrame
print(df.head())

# Perform operations like filtering, aggregating, etc.
filtered_data = df[df[] > some_value]


import pandas as pd

# Function to load data from a CSV file
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"The file at {file_path} was not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

# Ask for file paths
file_path_1 = input("Please enter the path to your first CSV file: ")
file_path_2 = input("Please enter the path to your second CSV file: ")

# Load the data from both files
df1 = load_data(file_path_1)
df2 = load_data(file_path_2)

if df1 is not None and df2 is not None:
    # Display the first few rows of both DataFrames
    print("First DataFrame:")
    print(df1.head())
    print("\nSecond DataFrame:")
    print(df2.head())

    # TODO: Combine the two DataFrames if necessary
    # For example, if both DataFrames have the same structure:
    combined_df = pd.concat([df1, df2])

    # TODO: Perform operations on the combined DataFrame
    # Such as filtering, aggregating, and plotting

    # Example operation: Filtering the combined DataFrame
    # Replace 'price_column' with the actual column name for price
    price_column = 'price'  # Replace with the actual price column name
    high_price_filter = combined_df[price_column] > 20  # Example filter condition
    high_price_data = combined_df[high_price_filter]
    print("\nFiltered data with high prices:")
    print(high_price_data)

    # Example of aggregating - calculating the mean price
    mean_price = combined_df[price_column].mean()
    print(f"\nThe mean price is: {mean_price}")

    # TODO: Implement further data analysis and visualization as required
else:
    print("One or both DataFrames were not loaded successfully.")


