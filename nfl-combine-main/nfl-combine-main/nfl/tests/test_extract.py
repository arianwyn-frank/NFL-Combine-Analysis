from features.extract import extract_data

def test_combine_data_loading():
    # Test if the combinedata DataFrame is not empty after loading
    combinedata, fantasydata = extract_data()
    assert not combinedata.empty, "Combinedata DataFrame is empty after loading"

def test_fantasy_data_loading():
    # Test if the fantasydata DataFrame is not empty after loading
    combinedata, fantasydata = extract_data()
    assert not fantasydata.empty, "Fantasydata DataFrame is empty after loading"

