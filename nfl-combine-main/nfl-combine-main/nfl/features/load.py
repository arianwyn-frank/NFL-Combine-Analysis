import pandas as pd
from transform import transform_data

def load_data_to_csv(data, file_path):
    """
    Save a DataFrame to a CSV file.

    Parameters:
    data (pd.DataFrame): The data to be saved.
    file_path (str): The path to the CSV file.
    """
    try:
        data.to_csv(file_path, index=False)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving data to CSV: {e}")

if __name__ == "__main__":
    # Get the transformed data from transform.py
    transformed_data = transform_data()

    # Define the path for the CSV file
    file_path = 'transformed_data.csv'

    # Save the transformed data to CSV
    load_data_to_csv(transformed_data, file_path)