def count_customers_by_gender(data):
    male_count = 0
    female_count = 0

    for row in data:
        gender = row["Customer_Gender"].strip().lower()

        if gender == "male":
            male_count += 1
        elif gender == "female":
            female_count += 1

    return male_count, female_count