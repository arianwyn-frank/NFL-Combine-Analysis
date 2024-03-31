import pandas as pd
from extract import extract_data

def transform_data():
    # Call the load_data function to get the data
    combinedata, fantasydata = extract_data()

    # Clean combine_data
    drafted_split = combinedata['Drafted (tm/rnd/yr)'].str.split('/', expand=True)

    # Assign new columns to the main DataFrame
    combinedata['DraftedTeam'] = drafted_split[0]
    combinedata['DraftedRound'] = drafted_split[1].str.extract(r'(\d+)').astype(float)  # Extract round number as float
    combinedata['DraftedYear'] = drafted_split[2].str.extract(r'(\d{4})').astype(float)  # Extract year as float

    # Drop the original 'Drafted (tm/rnd/yr)' column
    combinedata.drop(columns=['Drafted (tm/rnd/yr)'], inplace=True)

    # Handling the 'Age' column
    # Split the 'Age' column into two new columns 'Starting Age' and 'Ending Age'
    age_split = fantasydata['Age'].str.split('-', expand=True)
    fantasydata['Starting Age'] = pd.to_numeric(age_split[0], errors='coerce')
    fantasydata['Ending Age'] = pd.to_numeric(age_split[1], errors='coerce')

    # Where 'Ending Age' is NaN, it means there was no range, so copy 'Starting Age' to 'Ending Age'
    fantasydata['Ending Age'].fillna(fantasydata['Starting Age'], inplace=True)

    # Drop the original 'Age' column
    fantasydata.drop(columns=['Age'], inplace=True)
    
    # Sort only common players
    merged_data = pd.merge(combinedata, fantasydata, on='Player', how='inner')
    return merged_data

if __name__ == "__main__":
    # Call the transform function
    transformed_data = transform_data()