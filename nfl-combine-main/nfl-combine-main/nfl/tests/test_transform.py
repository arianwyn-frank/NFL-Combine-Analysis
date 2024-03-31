from features.transform import transform_data
from features.extract import extract_data
import pandas as pd
import pytest


def test_transformed_data_columns():
    # Test if the transformed data has the expected columns after calling transform_data
    transformed_data = transform_data()
    expected_columns = ['Player', 'Pos', 'School', 'Wt', '40yd', 'Vertical', 'Bench',
       'Broad Jump', '3Cone', 'Shuttle', 'DraftedTeam', 'DraftedRound',
       'DraftedYear', 'Rank', 'PPR/G', 'FirstSeason', 'LastSeason',
       'GamesPlayed', 'GamesStarted', 'TotalFantasyPoints',
       'TotalPprFantasyPoints', 'FantasyPointsPerGame',
       'PprFantasyPointsPerGame', 'Position', 'Team', 'Starting Age',
       'Ending Age']
    missing_columns = [column for column in expected_columns if column not in transformed_data.columns]

    assert not missing_columns, f"Missing columns in the transformed data: {missing_columns}"


def test_draft_round_values():
    # Test if the 'DraftedRound' column has valid values (positive floats or NaN) after calling transform_data
    transformed_data = transform_data()
    invalid_draft_round_values = [
        round_val for round_val in transformed_data['DraftedRound'] if not (
            pd.isna(round_val) or (isinstance(round_val, float) and round_val > 0)
        )
    ]
    print("Invalid DraftedRound values:", invalid_draft_round_values)
    assert not invalid_draft_round_values, f"Invalid values in DraftedRound: {invalid_draft_round_values}"


def test_age_values():
    # Test if the 'Starting Age' and 'Ending Age' columns have valid values (positive integers or NaN) after calling transform_data
    transformed_data = transform_data()
    age_columns = ['Starting Age', 'Ending Age']
    
    invalid_age_values = [
        (column, age_val) for column in age_columns for age_val in transformed_data[column] if not (
            pd.isna(age_val) or (isinstance(age_val, float) and age_val > 0)
        )
    ]
    print(transformed_data.columns)
    assert not invalid_age_values, f"Invalid values in Age columns: {invalid_age_values}"
