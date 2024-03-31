# import pandas as pd
# import pytest
# from transform import transform_data
# from extract import extract_data

# # Assuming 'extract_data' function is defined somewhere
# # TODO: The sample data below is not used by Pytest currently, need to find out why

# def alternative_extract():
#     # Implement an alternative extract function for testing
#     # Return sample data for testing
#     combinedata = pd.DataFrame({
#         "Player": ["Rashidi Barnes", "Sandy Johnson", "Mike Smith"],
#         "School": ["Baylor", "Wake Forest", "WashU"],
#         'Drafted (tm/rnd/yr)': ['1st / 1st pick / 2020', '2nd / 15th pick / 2019', '3rd / 10th pick / 2018'],
#         "Wt": [253, 190, 205],
#     })
#     fantasydata = pd.DataFrame({
#         "Position":["QB", "RB", "WR"],
#         "Player": ["Sandy Johnson", "Rashidi Barnes", "Hikari Watahime"],
#         "Age":[21, 24, 22],
#     })

#     return combinedata, fantasydata

# # @pytest.fixture
# # def sample_data():
# #     # You can modify this fixture to return sample data for testing
# #     return extract_data()

# @pytest.mark.parametrize("extract_function", [alternative_extract])
# def test_transform(monkeypatch, extract_function):

#     # Monkey patch the extract function with the alternative_extract function
#     # monkeypatch.setattr('extract.extract_data', extract_function)

#     # Call the transform function with the sample data
#     result = transform_data()

#     # Check if the result is a DataFrame
#     assert isinstance(result, pd.DataFrame)

#     # Add more specific checks based on your requirements
#     # For example, check if certain columns exist or have the expected values
#     assert 'Player' in result.columns
#     assert 'Drft 0' in result.columns
#     assert 'Drft 1' in result.columns
#     assert 'Drft 2' in result.columns

#     # Check if the merged_data DataFrame has the expected number of rows
#     expected_number_of_rows = 2199
#     assert len(result) == expected_number_of_rows

#     # Maybe add more detailed checks 
