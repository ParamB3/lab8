import data
from functions import (
    totalDeforestation,
    isHighDeforestation,
    compareYears,
    sustainabilityMessage
)
def percentChange(old: float, new: float) -> str:
    if old == 0:
        return "N/A"
    change = ((new - old) / old) * 100
    return f"{change:.1f}%"


def yearValue(year_obj):
    return year_obj.year


def amzValue(year_obj):
    return year_obj.amz


def dictValue(item):
    return item[1]


def generate_report(
    output_file: str = "deforestation_summary.txt",
    high_threshold: int = 10000
) -> None:

    years = data.load_deforestation_years()
    years = sorted(years, key=yearValue)

    if not years:
        print("No data found. Report not created.")
        return

    totals_by_year = totalDeforestation(years)

    first_year = years[0]
    last_year = years[-1]

    highest = max(years, key=amzValue)
    lowest = min(years, key=amzValue)

    high_years = []
    for y in years:
        if isHighDeforestation(y, high_threshold):
            high_years.append(y)

    yoy_changes = {}
    for i in range(1, len(years)):
        previous = years[i - 1]
        current = years[i]
        yoy_changes[current.year] = current.amz - previous.amz

    biggest_increase = None
    biggest_decrease = None

    if yoy_changes:
        biggest_increase = max(yoy_changes.items(), key=dictValue)
        biggest_decrease = min(yoy_changes.items(), key=dictValue)

    with open(output_file, "w", encoding="utf-8") as f:

        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write("AMAZON DEFORESTATION DATA ANALYSIS REPORT\n")
        f.write("=" * 80 + "\n\n")

        f.write("I. DATASET OVERVIEW\n")
        f.write("-" * 80 + "\n")
        f.write(f"Years Analyzed: {first_year.year} – {last_year.year}\n")
        f.write(f"Total Years in Dataset: {len(years)}\n")
        f.write(f"High Deforestation Threshold: {high_threshold:,} km²\n\n")

        f.write("II. SUMMARY STATISTICS\n")
        f.write("-" * 80 + "\n")
        f.write(f"Highest Deforestation Year : {highest.year} ({highest.amz:,.0f} km²)\n")
        f.write(f"Lowest Deforestation Year  : {lowest.year} ({lowest.amz:,.0f} km²)\n")
        f.write(f"Years Above Threshold      : {len(high_years)}\n")

        net_change = last_year.amz - first_year.amz
        f.write(f"Net Change (First → Last)  : {net_change:+,.0f} km²\n")
        f.write(f"Percent Change             : {percentChange(first_year.amz, last_year.amz)}\n")

        if biggest_increase:
            yr, val = biggest_increase
            f.write(f"Largest Yearly Increase    : {yr} ({val:+,.0f} km²)\n")

        if biggest_decrease:
            yr, val = biggest_decrease
            f.write(f"Largest Yearly Decrease    : {yr} ({val:+,.0f} km²)\n")

        f.write("\nIII. YEAR-BY-YEAR ANALYSIS\n")
        f.write("-" * 80 + "\n")

        for i in range(len(years)):
            year = years[i]

            f.write(f"\nYear: {year.year}\n")
            f.write(f"Deforestation Total: {year.amz:,.0f} km²\n")

            if isHighDeforestation(year, high_threshold):
                status = "HIGH DEFORESTATION"
            else:
                status = "Below Critical Threshold"

            f.write(f"Status: {status}\n")

            if i > 0:
                previous = years[i - 1]
                change = year.amz - previous.amz
                f.write(f"Change from {previous.year}: {change:+,.0f} km²\n")
            else:
                f.write("Change from Previous Year: N/A\n")

            f.write(f"Sustainability Insight: {sustainabilityMessage(year)}\n")

        f.write("\nIV. OVERALL TREND COMPARISON\n")
        f.write("-" * 80 + "\n")
        f.write(compareYears(last_year, first_year) + "\n")

        f.write("\nV. SOCIAL RESPONSIBILITY INTERPRETATION\n")
        f.write("-" * 80 + "\n")
        f.write(
            "Deforestation significantly impacts biodiversity, carbon emissions, "
            "indigenous communities, and long-term climate stability.\n"
        )
        f.write(
            "Identifying high-risk years allows governments and organizations "
            "to intervene with stronger environmental protections.\n"
        )

        f.write("\nVI. RECOMMENDATIONS\n")
        f.write("-" * 80 + "\n")
        f.write("- Strengthen monitoring during high-risk years.\n")
        f.write("- Support sustainable land-use policies.\n")
        f.write("- Increase transparency in supply chains.\n")
        f.write("- Use data-driven decision making for conservation funding.\n")

        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write("END OF REPORT\n")
        f.write("=" * 80 + "\n")

    print(f"\nReport successfully written to '{output_file}'\n")


if __name__ == "__main__":
    generate_report()