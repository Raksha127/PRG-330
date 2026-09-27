def analyze_data(clean):
    print("\nAverage Daily Rate:")
    print(
        round(
            clean["adr"].mean(),
            2
        )
    )

    print("\nAverage ADR by hotel:")
    print(
        clean.groupby(
            "hotel"
        )["adr"]
        .mean()
        .round(2)
    )

    print("\nBookings by hotel:")
    print(
        clean["hotel"].value_counts()
    )

    cancellation_rate = (
        clean["is_canceled"].mean()
        * 100
    )

    print("\nCancellation rate:")
    print(
        round(
            cancellation_rate,
            2
        )
    )

    print("\nCancellation by hotel:")
    hotel_cancellation = (
        clean.groupby(
            "hotel"
        )["is_canceled"]
        .agg(
            ["count", "mean"]
        )
    )

    hotel_cancellation["mean"] = (
        hotel_cancellation["mean"]
        * 100
    )

    print(
        hotel_cancellation.round(2)
    )

    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    monthly_bookings = (
        clean["arrival_date_month"]
        .value_counts()
        .reindex(month_order)
    )

    print("\nBookings by month:")
    print(monthly_bookings)

    print("\nTop 10 countries:")
    print(
        clean["country"]
        .value_counts()
        .head(10)
    )

    print("\nCustomer types:")
    print(
        clean["customer_type"]
        .value_counts()
    )

    print("\nAverage ADR by market segment:")
    print(
        clean.groupby(
            "market_segment"
        )["adr"]
        .mean()
        .sort_values(
            ascending=False
        )
        .round(2)
    )

    print("\nLead time by cancellation:")
    print(
        clean.groupby(
            "is_canceled"
        )["lead_time"]
        .agg(
            [
                "count",
                "mean",
                "median",
                "min",
                "max"
            ]
        )
        .round(2)
    )

    print("\nAverage length of stay:")
    print(
        round(
            clean["total_nights"].mean(),
            2
        )
    )

    print("\nLongest stays:")
    print(
        clean.sort_values(
            "total_nights",
            ascending=False
        )[
            [
                "hotel",
                "arrival_date_month",
                "total_nights",
                "adults",
                "children"
            ]
        ].head(10)
    )

    print("\nHighest estimated revenue:")
    print(
        clean.sort_values(
            "estimated_revenue",
            ascending=False
        )[
            [
                "hotel",
                "adr",
                "total_nights",
                "estimated_revenue"
            ]
        ].head(10)
    )

    print("\nRepeated guest and cancellation:")
    print(
        clean.groupby(
            "is_repeated_guest"
        )["is_canceled"]
        .agg(
            ["count", "mean"]
        )
        .round(3)
    )

    print("\nDeposit type and cancellation:")
    print(
        clean.groupby(
            "deposit_type"
        )["is_canceled"]
        .agg(
            ["count", "mean"]
        )
        .round(3)
    )

    print("\nSpecial requests and cancellation:")
    print(
        clean.groupby(
            "total_of_special_requests"
        )["is_canceled"]
        .mean()
        .round(3)
    )

    correlation = clean[
        [
            "lead_time",
            "adr",
            "total_nights",
            "total_guests",
            "booking_changes",
            "previous_cancellations",
            "total_of_special_requests",
            "is_canceled"
        ]
    ].corr()

    print("\nCorrelation:")
    print(
        correlation.round(3)
    )

    return correlation