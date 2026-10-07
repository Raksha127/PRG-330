from load_data import load_data
from predict import predict_date
from prepare_data import prepare_data
from train_model import train_model


def main():
    file_path = "Kathmandu_Daily_Climate_Data.csv"
    selected_date = "2020-07-03"

    print("Kathmandu Rainfall Prediction")
    print("-----------------------------")
    print()

    df = load_data(file_path)
    print(f"Dataset rows: {len(df)}")
    print()

    data, features = prepare_data(df)

    print("Training Linear Regression...")
    print()
    model, train_data, test_data, mae, r2 = train_model(data, features, selected_date)

    print()
    print("Model Evaluation")
    print(f"MAE: {mae:.2f} mm")
    print(f"R2: {r2:.2f}")
    print()

    result = predict_date(model, data, features, selected_date, test_data)

    print("Demo Prediction")
    print("---------------")
    print()
    print(f"Selected Date: {result['selected_date']}")
    print()
    print(f"Today's Rainfall: {result['today_rainfall']:.2f} mm")
    print(f"Previous 3-Day Rainfall: {result['previous_3d_rainfall']:.2f} mm")
    print(f"Humidity: {result['humidity']:.2f} %")
    print(f"Temperature: {result['temperature']:.2f} C")
    print(f"Pressure: {result['pressure']:.2f} kPa")
    print()
    print("Prediction period:")
    print(f"{result['prediction_start']} to {result['prediction_end']}")
    print()
    print(
        "Predicted Next 3-Day Rainfall: "
        f"{result['predicted_next_3d_rainfall']:.2f} mm"
    )
    print(f"Actual Next 3-Day Rainfall: {result['actual_next_3d_rainfall']:.2f} mm")
    print()
    print(f"Rainfall-Based Flood Risk: {result['risk_level']}")
    print(result["risk_message"])


if __name__ == "__main__":
    main()
