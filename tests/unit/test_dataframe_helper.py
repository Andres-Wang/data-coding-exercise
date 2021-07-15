import pandas as pd
import pytest

from modules.helpers.dataframe_helper import one_to_one_mappings_from_df


def test_one_to_one_mappings_from_df_positive():
    data = {"Fruit": ["Apple", "Banana", "Cherry"],
            "Colour": ["Red", "Yellow", "Red"]}
    df = pd.DataFrame(data=data)
    expected_mapping = {"Apple": "Red",
                        "Banana": "Yellow",
                        "Cherry": "Red"}
    assert one_to_one_mappings_from_df(df=df, index_col="Fruit", value_col="Colour") == expected_mapping


def test_one_to_one_mappings_from_df_negative():
    data = {"Fruit": ["Apple", "Banana", "Apple"],
            "Colour": ["Red", "Yellow", "Red"]}
    df = pd.DataFrame(data=data)
    with pytest.raises(ValueError) as excinfo:
        one_to_one_mappings_from_df(df=df, index_col="Fruit", value_col="Colour")
    assert str(excinfo.value) == "Fruit field contains duplicate value."
