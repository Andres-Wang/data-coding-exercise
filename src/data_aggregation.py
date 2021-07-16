def aggregate_sum_components_by_colour(df_orders, components_mapping, results):

    # column filtering to get needed fields only
    df_units = df_orders[["units"]]

    for _, row in df_units.iterrows():
        units = row["units"]
        for componentId in units:
            if componentId in components_mapping:
                colour = components_mapping[componentId]
            else:
                raise ValueError(f"{componentId} is not found in given components-colour mapping.")
            num_component = units[componentId]
            if num_component < 0:
                raise ValueError("There is negative value in the units column.")
            results[colour] += units[componentId]
