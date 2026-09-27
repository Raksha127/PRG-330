import pandas as pd

def load_data():
    df = pd.read_csv("hotel_bookings.csv")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)

    print("\nInfo:")
    df.info()

    print("\nBasic statistics:")
    print(df.describe())

    print("\nHotel:")
    print(df["hotel"].value_counts(dropna=False))

    print("\nMeal:")
    print(df["meal"].value_counts(dropna=False))

    print("\nMarket segment:")
    print(df["market_segment"].value_counts(dropna=False))

    print("\nCustomer type:")
    print(df["customer_type"].value_counts(dropna=False))

    print("\nDeposit type:")
    print(df["deposit_type"].value_counts(dropna=False))

    return df