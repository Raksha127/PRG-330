def prepare_data(df):
    """Create past-rainfall features and the next-3-day rainfall target."""
    data = df.copy()

    data["rain_1d_ago"] = data["PRECTOTCORR"].shift(1)
    data["rain_2d_ago"] = data["PRECTOTCORR"].shift(2)
    data["rain_3d_ago"] = data["PRECTOTCORR"].shift(3)

    data["prev_3d_rain"] = (
        data["rain_1d_ago"] + data["rain_2d_ago"] + data["rain_3d_ago"]
    )

    # These shifted target values are future rainfall totals used only as labels.
    data["next_3d_rain"] = (
        data["PRECTOTCORR"].shift(-1)
        + data["PRECTOTCORR"].shift(-2)
        + data["PRECTOTCORR"].shift(-3)
    )

    feature_columns = ["PRECTOTCORR", "prev_3d_rain", "RH2M", "T2M", "PS"]

    needed_columns = feature_columns + ["next_3d_rain", "DATE"]
    data = data.dropna(subset=needed_columns).reset_index(drop=True)

    return data, feature_columns
