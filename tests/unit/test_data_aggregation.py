import pandas as pd
from collections import defaultdict
from src.data_aggregation import aggregate_sum_components_by_colour


def test_aggregate_sum_components_by_colour():
    results = defaultdict(int)
    data = {"units": [{"XNPRP05": 5, "BKRED01": 23}, {"BKRED01": 9, "BBBBK00": 3}]}
    components_mapping = {'BKRED01': 'Red', 'BKONG13': 'Orange', 'BKYLW88': 'Yellow', 'BKGRN02': 'Green',
                          'XXBLU99': 'Blue', 'XNPRP05': 'Purple', 'BBBRN71': 'Brown', 'BBBBK00': 'Black',
                          'KNWHI01': 'White', 'ZZGLD01': 'Gold'}
    df_orders = pd.DataFrame(data=data)
    aggregate_sum_components_by_colour(df_orders=df_orders,
                                       components_mapping=components_mapping,
                                       results=results)

    assert results == {'Purple': 5, 'Red': 32, 'Black': 3}
