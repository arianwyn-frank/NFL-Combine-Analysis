
  
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


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {}
    key = '.'.join(args)
    return dbt_load_df_function(sources[key])


config_dict = {}


class config:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get(key, default=None):
        return config_dict.get(key, default)

class this:
    """dbt.this() or dbt.this.identifier"""
    database = "dev"
    schema = "main"
    identifier = "extract_combine"
    
    def __repr__(self):
        return '"dev"."main"."extract_combine"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------




def materialize(df, con):
    try:
        import pyarrow
        pyarrow_available = True
    except ImportError:
        pyarrow_available = False
    finally:
        if pyarrow_available and isinstance(df, pyarrow.Table):
            # https://github.com/duckdb/duckdb/issues/6584
            import pyarrow.dataset
    con.execute('create table "dev"."main"."extract_combine__dbt_tmp" as select * from df')

  