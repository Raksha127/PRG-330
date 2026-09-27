import matplotlib.pyplot as plt

def visualize_data(clean):
    clean[
        clean["adr"] < 1000
    ]["adr"].plot(
        kind="hist",
        bins=30,
        edgecolor="black"
    )

    plt.title(
        "Distribution of Average Daily Rate"
    )

    plt.xlabel(
        "Average Daily Rate"
    )

    plt.ylabel(
        "Number of Bookings"
    )

    plt.tight_layout()
    plt.show()

    clean[
        "hotel"
    ].value_counts().plot(
        kind="bar"
    )

    plt.title(
        "Bookings by Hotel Type"
    )

    plt.xlabel(
        "Hotel"
    )

    plt.ylabel(
        "Number of Bookings"
    )

    plt.xticks(
        rotation=0
    )

    plt.tight_layout()
    plt.show()

    clean[
        clean["adr"] < 1000
    ].plot(
        x="lead_time",
        y="adr",
        kind="scatter",
        alpha=0.2
    )

    plt.title(
        "Lead Time vs Average Daily Rate"
    )

    plt.xlabel(
        "Lead Time"
    )

    plt.ylabel(
        "Average Daily Rate"
    )

    plt.tight_layout()
    plt.show()