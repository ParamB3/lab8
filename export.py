#Param Butani
from functions import (
    totalDeforestation,
    isHighDeforestation,
    compareYears,
    sustainabilityMessage,
    i_include_year
)
#Jorge Sanchez
import data
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

#Both (We split it by sections)
def generate_report(
        #Jorge
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
#Param Butani
        f.write("1. DATASET OVERVIEW\n")
        f.write(f"Years Analyzed: {first_year.year} – {last_year.year}\n")
        f.write(f"Total Years in Dataset: {len(years)}\n")
        f.write(f"High Deforestation Threshold: {high_threshold:,} km²\n\n")
#Param Butani
        f.write("2. SUMMARY STATISTICS\n")
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
#Jorge Sanchez
        f.write("\n3. YEAR-BY-YEAR ANALYSIS\n")
        f.write("-" * 60 + "\n")

        for i in range(len(years)):
            year = years[i]

            f.write(f"\nYear: {year.year}\n")
            f.write(f"Deforestation Total: {year.amz:,.0f} km²\n")

            climate_events = data.loadClimateEvents()
            events_this_year = []
            for ev in climate_events:
                if i_include_year(ev, year.year):
                    events_this_year.append(ev.event)

            if events_this_year:
                f.write("Climate Event: " + ", ".join(events_this_year) + "\n")
            else:
                f.write("Climate Event: None Recorded\n")
                status = "HIGH DEFORESTATION" if isHighDeforestation(year, high_threshold) else "Below Critical Threshold"
                f.write(f"Status: {status}\n")

            if i > 0:
                previous = years[i - 1]
                change = year.amz - previous.amz
                f.write(f"Change from {previous.year}: {change:+,.0f} km²\n")
            else:
                f.write("Change from Previous Year: N/A\n")

            f.write(f"Sustainability Insight: {sustainabilityMessage(year)}\n")
#Jorge Sanchez
        f.write("\n4. OVERALL TREND COMPARISON\n")
        f.write(compareYears(last_year, first_year) + "\n")
#Jorge Sanchez
        f.write("\n5. SOCIAL RESPONSIBILITY INTERPRETATION\n")
        f.write("-" * 80 + "\n")
        f.write(
            "There are massive impacts of deforestation throughout the world."
            "These include indigenous communities, biodiversity, carbon emissions and long-term climate stability in general.\n"
        )
        f.write(
            "This problem can be greatly aided by identifying high-risk years."
            "This allows governments and organizations to implement environmental protections.\n"
        )
#Param Butani
        f.write("\n6. RECOMMENDATIONS\n")
        f.write("-" * 80 + "\n")
        f.write("- Analyse external variables that impact High Risk or High Severity years\n")
        f.write("- Support sustainable land-use policies.\n")
        f.write("- Increase transparency in supply chains.\n")
        f.write("- Force mega corporations to take on policies for environmental safety\n")
        f.write("On conclusion, there are many aspects of deforestation that are ruining our land.\n")
        f.write("In order to fix these, we have to implement the strategies that have were mentioned above.\n")


if __name__ == "__main__":
    generate_report()