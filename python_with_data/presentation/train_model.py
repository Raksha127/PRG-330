import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def _find_split_index(data, selected_date=None, train_ratio=0.8):
    split_index = int(len(data) * train_ratio)

    if selected_date is None:
        return split_index

    selected_date = pd.to_datetime(selected_date)
    matching_rows = data.index[data["DATE"] == selected_date].tolist()

    if not matching_rows:
        raise ValueError(f"Selected date {selected_date.date()} was not found in the data.")

    selected_index = matching_rows[0]

    # If the demo date would be trained on, move it into the test section.
    if selected_index < split_index:
        split_index = selected_index

    if split_index <= 0 or split_index >= len(data):
        raise ValueError("Cannot create a valid chronological train/test split.")

    return split_index


def train_model(data, features, selected_date=None):
    split_index = _find_split_index(data, selected_date)

    train_data = data.iloc[:split_index].copy()
    test_data = data.iloc[split_index:].copy()

    X_train = train_data[features]
    y_train = train_data["next_3d_rain"]
    X_test = test_data[features]
    y_test = test_data["next_3d_rain"]

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Training rows: {len(train_data)}")
    print(f"Testing rows: {len(test_data)}")
    print(f"MAE: {mae:.2f} mm")
    print(f"R2: {r2:.2f}")

    return model, train_data, test_data, mae, r2
