from load_data import load_data
from identify_data_issues import identify_data_issues
from clean_data import clean_data
from analyze_data import analyze_data
from visualization import visualize_data
from export_results import export_results

df = load_data()

identify_data_issues(df)

clean = clean_data(df)

correlation = analyze_data(clean)

visualize_data(clean)

export_results(
    clean,
    correlation
)