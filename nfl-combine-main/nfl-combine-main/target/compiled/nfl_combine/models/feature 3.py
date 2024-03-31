import pandas as pd
from transform import transform_data
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score

def filter_data():
    merged_data = transform_data()
    columns_to_drop = ['Pos', 'School', 'Position', 'Team', 'TotalPprFantasyPoints', 'FantasyPointsPerGame',
       'PprFantasyPointsPerGame', 'Player', 'DraftedTeam']
    merged_data.drop(columns=columns_to_drop, inplace=True)
    merged_data = merged_data[merged_data['LastSeason'] < 2023]
    merged_data['YearsPlayed'] = merged_data['LastSeason'] - merged_data['FirstSeason']
    return merged_data

def model(dbt, session):  
    merged_data = transform_data()
    columns_to_drop = ['Pos', 'School', 'Position', 'Team', 'TotalPprFantasyPoints', 'FantasyPointsPerGame',
       'PprFantasyPointsPerGame', 'Player', 'DraftedTeam']
    merged_data.drop(columns=columns_to_drop, inplace=True)
    merged_data = merged_data[merged_data['LastSeason'] < 2023]
    merged_data['YearsPlayed'] = merged_data['LastSeason'] - merged_data['FirstSeason']
    return merged_data

def train_model():
    filtered_data = filter_data()
    features = ['Wt', '40yd', 'Vertical', 'Bench', 'Broad Jump', '3Cone', 'Shuttle']
    target = ['TotalFantasyPoints']
    
    # Separate features and target variable
    X = filtered_data[features]
    y = filtered_data[target]
    
    # Handle missing values in features
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    target_variable_range = filtered_data[target].max() - filtered_data[target].min()
    print(f"The range of the target variable '{target}' is: {target_variable_range}")
    
    return model


def predict_years_played(model, input_stats):
    # Convert input_stats to a DataFrame with the same columns as the training data
    input_df = pd.DataFrame([input_stats], columns=['Wt', '40yd', 'Vertical', 'Bench', 'Broad Jump', '3Cone', 'Shuttle'])
    
    # Make predictions
    predicted_years = model.predict(input_df)
    
    return predicted_years[0][0]


def evaluate_model(model, X_test, y_test, imputer):
    # Handle missing values in features (X_test)
    X_test_imputed = imputer.transform(X_test)

    # Make predictions
    y_pred = model.predict(X_test_imputed)

    # Calculate MSE and RMSE
    mse = mean_squared_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Calculate R2 score
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error (MSE): {mse}')
    print(f'Root Mean Squared Error (RMSE): {rmse}')
    print(f'R-squared (R2 Score): {r2}')


if __name__ == "__main__":
    # Get the filtered data
    filtered_data = filter_data()

    # Train the model
    trained_model = train_model()

    # Split the data into training and testing sets
    features = ['Wt', '40yd', 'Vertical', 'Bench', 'Broad Jump', '3Cone', 'Shuttle']
    target = ['TotalFantasyPoints']
    X = filtered_data[features]
    y = filtered_data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Handle missing values in features for both training and testing data
    imputer = SimpleImputer(strategy='mean')
    X_train_imputed = imputer.fit_transform(X_train)
    
    # Fit the imputer to the training data and transform the testing data
    X_test_imputed = imputer.transform(X_test)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train_imputed, y_train)

    # Evaluate the model
    evaluate_model(model, X_test_imputed, y_test, imputer)


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
    identifier = "feature 3"
    
    def __repr__(self):
        return '"dev"."main"."feature 3"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


