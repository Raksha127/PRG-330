def identify_data_issues(df):
    missing = df.isna().sum()

    print("\nMissing values:")
    print(missing)

    print("\nColumns with missing values:")
    print(
        missing[missing > 0]
        .sort_values(ascending=False)
    )

    missing_pct = (
        df.isna().sum() / len(df)
    ) * 100

    print("\nMissing value percentages:")
    print(
        missing_pct[missing_pct > 0]
        .sort_values(ascending=False)
        .round(2)
    )

    duplicate_rows = df.duplicated().sum()

    print("\nDuplicate rows:")
    print(duplicate_rows)

    print("\nSample duplicate rows:")
    print(
        df[df.duplicated()].head(10)
    )

    bad_adr = df[df["adr"] < 0]

    print("\nNegative ADR values:")
    print(bad_adr)

    total_guests = (
        df["adults"]
        + df["children"].fillna(0)
        + df["babies"]
    )

    bad_guests = df[
        total_guests <= 0
    ]

    print("\nBookings with no guests:")
    print(
        bad_guests[
            [
                "hotel",
                "adults",
                "children",
                "babies"
            ]
        ].head(20)
    )

    checks = {
        "lead_time": (0, 1000),
        "stays_in_weekend_nights": (0, 50),
        "stays_in_week_nights": (0, 100),
        "adults": (0, 100),
        "children": (0, 20),
        "babies": (0, 20),
        "adr": (0, 10000),
        "required_car_parking_spaces": (0, 20),
        "total_of_special_requests": (0, 20)
    }

    print("\nNumeric range checks:")

    for col, (low, high) in checks.items():
        bad = (
            df[col].notna()
            &
            (
                (df[col] < low)
                |
                (df[col] > high)
            )
        )

        print(
            col,
            ":",
            bad.sum(),
            "invalid values"
        )