import pandas as pd

def clean_data(df):
    clean = df.copy()

    clean = clean.drop_duplicates()

    clean.loc[
        clean["adr"] < 0,
        "adr"
    ] = pd.NA

    clean["children"] = clean["children"].fillna(
        clean["children"].median()
    )

    clean["country"] = clean["country"].fillna(
        "Unknown"
    )

    clean["agent"] = clean["agent"].fillna(0)

    clean["company"] = clean["company"].fillna(0)

    clean["adr"] = clean["adr"].fillna(
        clean["adr"].median()
    )

    clean["total_guests"] = (
        clean["adults"]
        + clean["children"]
        + clean["babies"]
    )

    clean["total_nights"] = (
        clean["stays_in_weekend_nights"]
        + clean["stays_in_week_nights"]
    )

    clean["estimated_revenue"] = (
        clean["adr"]
        * clean["total_nights"]
    )

    print("\nRows after cleaning:")
    print(len(clean))

    print("\nMissing values after cleaning:")
    print(clean.isna().sum())

    print("\nDuplicate rows after cleaning:")
    print(clean.duplicated().sum())

    print("\nNegative ADR values:")
    print(
        (clean["adr"] < 0).sum()
    )

    return clean