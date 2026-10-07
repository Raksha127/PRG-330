import pandas as pd

from risk import get_risk, get_risk_message


def predict_date(model, data, features, selected_date, test_data=None):
    selected_date = pd.to_datetime(selected_date)

    if test_data is not None and selected_date not in set(test_data["DATE"]):
        raise ValueError(
            f"{selected_date.date()} is not inside the test set. "
            "Use a chronological split that keeps the demo date held out."
        )

    selected_rows = data[data["DATE"] == selected_date]
    if selected_rows.empty:
        raise ValueError(f"Selected date {selected_date.date()} was not found in the data.")

    row = selected_rows.iloc[0]

    X_demo = row[features].to_frame().T
    predicted_rain = float(model.predict(X_demo)[0])

    actual_rain = float(row["next_3d_rain"])
    risk_level = get_risk(predicted_rain)

    return {
        "selected_date": row["DATE"].date(),
        "today_rainfall": float(row["PRECTOTCORR"]),
        "previous_3d_rainfall": float(row["prev_3d_rain"]),
        "humidity": float(row["RH2M"]),
        "temperature": float(row["T2M"]),
        "pressure": float(row["PS"]),
        "prediction_start": (row["DATE"] + pd.Timedelta(days=1)).date(),
        "prediction_end": (row["DATE"] + pd.Timedelta(days=3)).date(),
        "predicted_next_3d_rainfall": predicted_rain,
        "actual_next_3d_rainfall": actual_rain,
        "risk_level": risk_level,
        "risk_message": get_risk_message(risk_level),
    }
