# Presentation Notes

## Project Topic

Kathmandu rainfall prediction using simple Linear Regression.

## Main Goal

Use weather information available on a selected date to predict the total
rainfall for the next 3 days.

## Important Limitation

This is not a real flood prediction model. The dataset does not contain actual
flood event labels or river-level measurements. The project only gives a simple
rainfall-based flood-risk indicator.

## Input Features

- Today's rainfall: `PRECTOTCORR`
- Previous 3-day rainfall: `prev_3d_rain`
- Humidity: `RH2M`
- Temperature: `T2M`
- Pressure: `PS`

## Target

`next_3d_rain` = rainfall tomorrow + rainfall after 2 days + rainfall after
3 days.

## Data Leakage Avoidance

Future rainfall is used only for the target value, not as an input feature.
The dataset is split chronologically, so the model trains on older records and
tests on newer records.

## Risk Levels

- LOW: predicted rainfall under 8 mm
- MODERATE: predicted rainfall from 8 mm to below 22.7 mm
- HIGH: predicted rainfall 22.7 mm or higher

## Demo Date

The project treats `2020-07-03` as today and predicts rainfall for
`2020-07-04` to `2020-07-06`.
