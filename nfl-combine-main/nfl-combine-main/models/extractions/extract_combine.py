# data_loader.py
import pandas as pd


def model(dbt, session):
    combinedata_url = "https://wustl.box.com/shared/static/6tneejtd0ijdy6ayhg04bn8juq9rhsd5.csv"
   

    # Read the CSV files into DataFrames
    combinedata = pd.read_csv(combinedata_url)

    return combinedata


# def model(dbt, session):
#     combinedata_url = "https://wustl.box.com/shared/static/6tneejtd0ijdy6ayhg04bn8juq9rhsd5.csv"
#     fantasydata_url = "https://wustl.box.com/shared/static/kwwagtq785dr67ze6y8xf4guwinkb0ai.csv"

#     # Read the CSV files into DataFrames
#     combinedata = pd.read_csv(combinedata_url)
#     fantasydata = pd.read_csv(fantasydata_url)

#     return combinedata, fantasydata

# def extract_data():
#     combinedata_url = "https://wustl.box.com/shared/static/6tneejtd0ijdy6ayhg04bn8juq9rhsd5.csv"
#     fantasydata_url = "https://wustl.box.com/shared/static/kwwagtq785dr67ze6y8xf4guwinkb0ai.csv"

#     # Read the CSV files into DataFrames
#     combinedata = pd.read_csv(combinedata_url)
#     fantasydata = pd.read_csv(fantasydata_url)

#     return combinedata, fantasydata

# if __name__ == "__main__":
#     # This block will only be executed if you run this script directly
#     # You can use it for testing or additional functionality if needed
#     combinedata, fantasydata = extract_data()

#     # Print or perform any other operations with the loaded data
#     print(combinedata.head())
#     print(fantasydata.head())


