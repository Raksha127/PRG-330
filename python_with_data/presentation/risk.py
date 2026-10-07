def get_risk(predicted_rain):
    if predicted_rain < 8:
        return "LOW"

    if predicted_rain < 22.7:
        return "MODERATE"

    return "HIGH"


def get_risk_message(risk_level):
    messages = {
        "LOW": "Low rainfall risk.",
        "MODERATE": "Moderate rainfall expected. Stay aware.",
        "HIGH": "Heavy rainfall may occur. Stay alert for local flood and river warnings.",
    }
    return messages[risk_level]
