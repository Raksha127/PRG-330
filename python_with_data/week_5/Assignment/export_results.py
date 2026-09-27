def export_results(clean, correlation):
    summary = clean.groupby(
        "hotel"
    ).agg(
        Bookings=(
            "hotel",
            "count"
        ),
        Average_ADR=(
            "adr",
            "mean"
        ),
        Average_Lead_Time=(
            "lead_time",
            "mean"
        ),
        Average_Stay=(
            "total_nights",
            "mean"
        ),
        Cancellation_Rate=(
            "is_canceled",
            "mean"
        ),
        Average_Guests=(
            "total_guests",
            "mean"
        )
    )

    summary[
        "Cancellation_Rate"
    ] = (
        summary[
            "Cancellation_Rate"
        ] * 100
    )

    summary = summary.round(2)

    customer_summary = clean.groupby(
        "customer_type"
    ).agg(
        Bookings=(
            "customer_type",
            "count"
        ),
        Average_ADR=(
            "adr",
            "mean"
        ),
        Average_Stay=(
            "total_nights",
            "mean"
        ),
        Cancellation_Rate=(
            "is_canceled",
            "mean"
        )
    )

    customer_summary[
        "Cancellation_Rate"
    ] = (
        customer_summary[
            "Cancellation_Rate"
        ] * 100
    )

    customer_summary = (
        customer_summary.round(2)
    )

    print("\nHotel summary:")
    print(summary)

    print("\nCustomer summary:")
    print(customer_summary)

    clean.to_csv(
        "hotel_bookings_cleaned.csv",
        index=False
    )

    summary.to_csv(
        "hotel_booking_summary.csv"
    )

    customer_summary.to_csv(
        "hotel_customer_summary.csv"
    )

    correlation.to_csv(
        "hotel_booking_correlation.csv"
    )

    print("\nFiles exported successfully")