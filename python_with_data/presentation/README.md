# Kathmandu Rainfall Prediction

This is a simple student machine learning project for predicting the total
rainfall for the next 3 days in Kathmandu.

The model uses `LinearRegression` from scikit-learn. It is not a direct flood
prediction model because the dataset does not include confirmed flood events or
river-level labels. The final risk level is only a rainfall-based indicator.

## Files

- `main.py` - runs the full project
- `load_data.py` - loads the CSV and creates the `DATE` column
- `prepare_data.py` - creates features and target values
- `train_model.py` - trains and evaluates the Linear Regression model
- `predict.py` - predicts rainfall for the selected demo date
- `risk.py` - converts predicted rainfall into LOW, MODERATE, or HIGH risk

## How To Run

Put `Kathmandu_Daily_Climate_Data.csv` in this same folder.

Install requirements:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

The demo date is `2020-07-03`. The program predicts total rainfall for
`2020-07-04` to `2020-07-06` and compares it with the actual value in the
historical data.
