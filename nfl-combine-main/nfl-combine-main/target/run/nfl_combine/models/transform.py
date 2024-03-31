
  
    import pandas as pd
from models.extractions.extract_combine import extract_data

# def transform_data():
def model(dbt, session):  
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
    identifier = "transform"
    
    def __repr__(self):
        return '"dev"."main"."transform"'


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
    con.execute('create table "dev"."main"."transform__dbt_tmp" as select * from df')

  