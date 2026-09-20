# Module 2: Loop Statement
# Finds the most popular product category

def find_popular_category(data):
    category_counts = {}

    for row in data:
        category = row["Product_Category"].strip()

        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    most_popular = max(category_counts, key=category_counts.get)
    count = category_counts[most_popular]

    return most_popular, count