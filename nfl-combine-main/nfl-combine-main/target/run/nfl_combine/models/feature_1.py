
  
    import pandas as pd
import transform_
import matplotlib.pyplot as plt
import seaborn as sns



def filter_data():
    merged_data = transform_.transform_data()
    columns_to_drop = ['Pos', 'School', 'Position', 'Team', 'TotalFantasyPoints', 'TotalPprFantasyPoints', 'FantasyPointsPerGame',
       'PprFantasyPointsPerGame', 'Player', 'DraftedTeam']
    merged_data.drop(columns=columns_to_drop, inplace=True)
    return merged_data

def get_qb_data():
    merged_data = transform_.transform_data()
    columns_to_drop = ['Pos', 'School', 'Team', 'TotalFantasyPoints', 'TotalPprFantasyPoints', 'FantasyPointsPerGame', 'PprFantasyPointsPerGame', 'Player', 'DraftedTeam']
    merged_data.drop(columns=columns_to_drop, inplace=True)

    # Filter to include only QBs
    qb_data = merged_data[merged_data['Position'] == 'QB']
    qb_data.drop(columns='Position', inplace=True)

    return qb_data

def model(dbt, session):

    merged_data = transform_.transform_data()
    columns_to_drop = ['Pos', 'School', 'Team', 'TotalFantasyPoints', 'TotalPprFantasyPoints', 'FantasyPointsPerGame', 'PprFantasyPointsPerGame', 'Player', 'DraftedTeam']
    merged_data.drop(columns=columns_to_drop, inplace=True)

    # Filter to include only QBs
    qb_data = merged_data[merged_data['Position'] == 'QB']
    qb_data.drop(columns='Position', inplace=True)

    return qb_data

if __name__ == "__main__":
    # Get the filtered data
    filtered_data = filter_data()

    # Compute the correlation matrix
    corr_matrix_all = filtered_data.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr_matrix_all, annot=True, fmt=".2f", cmap='coolwarm')

    # Show the plot
    plt.show()
    plt.savefig('correlation_heatmap.png')

    # Get the filtered data for QBs
    qb_data = get_qb_data()

    # Compute the correlation matrix
    corr_matrix_qb = qb_data.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr_matrix_qb, annot=True, fmt=".2f", cmap='coolwarm')

    # Show the plot
    plt.show()
    plt.savefig('correlation_heatmap_QBs.png')

    #print(filtered_data.columns)


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
    identifier = "feature_1"
    
    def __repr__(self):
        return '"dev"."main"."feature_1"'


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
    con.execute('create table "dev"."main"."feature_1__dbt_tmp" as select * from df')

  