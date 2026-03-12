import data
from functions import (
    totalDeforestation,
    isHighDeforestation,
    compareYears,
    sustainabilityMessage
)


def generate_report(output_file: str = "deforestation_summary.txt") -> None:
    years = data.load_deforestation_years()
    totals = totalDeforestation(years)
    with open(output_file, "w") as f:

        f.write("Amazon Deforestation Analysis Report\n")
        f.write("=" * 40 + "\n\n")
        for year in years:
            f.write(f"Year: {year.year}\n")
            f.write(f"Total Amazon Deforestation: {year.amz} km^2\n")

            if isHighDeforestation(year, 10000):
                f.write("Status: High Deforestation\n")
            else:
                f.write("Status: Below Critical Threshold\n")

            # Sustainability message
            f.write(f"Message: {sustainabilityMessage(year)}\n")
            f.write("-" * 30 + "\n")

        if len(years) >= 2:
            comparison = compareYears(years[-1], years[0])
            f.write("\nOverall Trend (First vs Last Year):\n")
            f.write(comparison + "\n")

    print(f"Report successfully written to '{output_file}'")


if __name__ == "__main__":
    generate_report()