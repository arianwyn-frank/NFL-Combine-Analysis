import pandas as pd

def model(dbt, session):
   
    fantasydata_url = "https://wustl.box.com/shared/static/kwwagtq785dr67ze6y8xf4guwinkb0ai.csv"

    # Read the CSV files into DataFrames

    fantasydata = pd.read_csv(fantasydata_url)

    return fantasydata