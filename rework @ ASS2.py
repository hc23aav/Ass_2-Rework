import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_file(file_path):
    """
    Reads a CSV file and returns a DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The DataFrame containing the data.
    """
    return pd.read_csv(file_path)

# Load the data using the function
data = read_file('weather-anomalies.csv')

def display_summary_info(data):
    """
    Displays summary statistics and information about the dataset.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the data.
    """
    print("Summary Statistics:")
    print(data.describe())
    print("\nInfo:")
    print(data.info())

# Display summary statistics and information about the dataset
display_summary_info(data)

# Initialize the flag to check for exception
exception_flag = False

# Histogram of Max Temperature
plt.figure(figsize=(8, 6))
try:
    data['max_temp'] = pd.to_numeric(data['max_temp'])  # Convert 'max_temp' to numeric
    data['max_temp'].plot(kind='hist', bins=20, edgecolor='black')
    plt.title('Distribution of Max Temperature')
    plt.xlabel('Max Temperature')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Scatter plot of Max Temperature vs Min Temperature
    plt.figure(figsize=(8, 6))
    data.plot(kind='scatter', x='max_temp', y='min_temp', alpha=0.7)
    plt.title('Max Temperature vs Min Temperature')
    plt.xlabel('Max Temperature')
    plt.ylabel('Min Temperature')
    plt.grid(True)
    plt.show()

   
    # Convert 'date_str' to datetime and sort the DataFrame by date
    data['date_str'] = pd.to_datetime(data['date_str'])
    data_sorted = data.sort_values(by='date_str')

    # Line plot of Degrees from Mean Over Time
    plt.figure(figsize=(10, 6))
    data_sorted.plot(x='date_str', y='degrees_from_mean')
    plt.title('Degrees from Mean Over Time')
    plt.xlabel('Date')
    plt.ylabel('Degrees from Mean')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    # Scatter plot of Latitude vs Longitude Colored by Max Temperature
    plt.figure(figsize=(8, 6))
    plt.scatter(data['longitude'], data['latitude'], c=data['max_temp'], cmap='coolwarm', alpha=0.5)
    plt.colorbar(label='Max Temperature')
    plt.title('Latitude vs Longitude Colored by Max Temperature')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()

    # Correlation matrix with transposition
    correlation_matrix = data.corr().transpose()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

except ValueError as e:
    print(f"Error: {e}")
    print("Please check the 'max_temp' column for non-numeric values.")
    # Set the flag to True if an exception occurs
    exception_flag = True

def create_pie_chart(data, exception_flag):
    """
    Creates a pie chart of Weather Type Distribution.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the data.
    - exception_flag (bool): Flag indicating if an exception occurred.
    """
    # Pie chart of Weather Type Distribution
    plt.figure(figsize=(8, 8))
    type_distribution = data['type'].value_counts()
    type_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Weather Types')
    plt.axis('equal')
    plt.show()

    # If there was an exception, print a message
    if exception_flag:
        print("Note: The pie chart was created despite the exception.")

# Create the pie chart
create_pie_chart(data, exception_flag)