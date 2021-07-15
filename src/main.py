import json
import logging

from modules.helpers.dataframe_helper import read_local_file_to_df, one_to_one_mappings_from_df, filter_df_by_timestamp
from collections import defaultdict
from data_aggregation import aggregate_sum_components_by_colour


def main():

    logging.getLogger().setLevel(logging.INFO)

    with open('src/config.json', 'r') as f:
        config = json.load(f)

    df_dim_components = read_local_file_to_df(file_path=config["local_data_files"]["dim_components"]["file_path"],
                                              file_format=config["local_data_files"]["dim_components"]["file_format"])

    # Fact tables may be large, read iteratively
    iter_df_fact_orders = read_local_file_to_df(file_path=config["local_data_files"]["fact_orders"]["file_path"],
                                                file_format=config["local_data_files"]["fact_orders"]["file_format"],
                                                chunk_size=config["local_data_files"]["fact_orders"]["chunk_size"])

    # Get componentId - colour mapping
    components_mapping = one_to_one_mappings_from_df(df=df_dim_components,
                                                     index_col=config["components_mapping"]["id_col"],
                                                     value_col=config["components_mapping"]["colour_col"])

    sum_of_components_by_colour = defaultdict(int)

    for df_order_chunk in iter_df_fact_orders:

        # row filtering
        df_filtered_orders = filter_df_by_timestamp(df=df_order_chunk,
                                                    timestamp_col=config["order_filter"]["timestamp_col"],
                                                    start_ts=config["order_filter"]["start_timestamp"],
                                                    end_ts=config["order_filter"]["end_timestamp"])

        aggregate_sum_components_by_colour(df_orders=df_filtered_orders,
                                           components_mapping=components_mapping,
                                           results=sum_of_components_by_colour)

    logging.info(f"Sum of components by colours in 2021/06/03: \n{dict(sum_of_components_by_colour)}")


if __name__ == '__main__':
    main()
