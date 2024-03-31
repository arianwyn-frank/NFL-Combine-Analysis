import pandas as pd
import pytest
from features.feature_1 import filter_data, get_qb_data
from features.feature_2 import filter_data, train_model, evaluate_model, predict_years_played
from features.feature_3 import filter_data, train_model, evaluate_model, predict_years_played
from features.transform import transform_data
from features.extract import extract_data
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


@pytest.fixture
# Tests for feature 1
def merged_data():
    return transform_data()

def test_filter_data_columns(merged_data):
    filtered_data = filter_data()
    assert all(column in filtered_data.columns for column in merged_data.columns), "Missing columns in filtered data"

def test_filter_data_size(merged_data):
    filtered_data = filter_data()
    assert len(filtered_data) <= len(merged_data), "Filtered data size is greater than original data size"

def test_get_qb_data_columns(merged_data):
    qb_data = get_qb_data()
    assert all(column in qb_data.columns for column in merged_data.columns), "Missing columns in QB data"

def test_get_qb_data_size(merged_data):
    qb_data = get_qb_data()
    assert len(qb_data) <= len(merged_data), "QB data size is greater than original data size"

# Tests for feature 2
def test_filter_data():
    test_data = pd.DataFrame({
        'Wt': [200, 210, 195],
        '40yd': [4.5, 4.8, 4.3],
        # Add other columns as needed
        'LastSeason': [2022, 2023, 2021]
    })

    result = filter_data(test_data)
    
    # Perform assertions based on the expected output
    assert 'YearsPlayed' in result.columns
    assert 'Wt' in result.columns
    assert result['YearsPlayed'].max() < 2023

# Test for the train_model function
def test_train_model():
    test_data = pd.DataFrame({
        'Wt': [200, 210, 195],
        '40yd': [4.5, 4.8, 4.3],
        # Add other columns as needed
        'LastSeason': [2022, 2023, 2021]
    })

    model = train_model(test_data)
    
    assert isinstance(model, LinearRegression)  


# Test for feature 3
# Test for train_model function
def test_train_model():
    test_data = pd.DataFrame({
        'Wt': [200, 210, 195],
        '40yd': [4.5, 4.8, 4.3],
        # Add other columns as needed
        'LastSeason': [2022, 2023, 2021]
    })

    model = train_model(test_data)
    
    # Perform assertions based on the expected behavior of the trained model
    assert isinstance(model, LinearRegression)