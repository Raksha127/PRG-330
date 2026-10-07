import pandas as pd


def load_data(file_path):
    """Load Kathmandu climate data and create a real DATE column."""
    df = pd.read_csv(file_path)

    required_columns = ["YEAR", "DOY", "PRECTOTCORR", "RH2M", "T2M", "PS"]
    missing_columns = [column for column in required_columns if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in dataset: {missing_columns}")

    df["DATE"] = pd.to_datetime(
        df["YEAR"].astype(int).astype(str),
        format="%Y",
    ) + pd.to_timedelta(df["DOY"].astype(int) - 1, unit="D")

    df = df.sort_values("DATE").reset_index(drop=True)
    return df
