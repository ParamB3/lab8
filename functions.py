import data
from classFile import deforestationYear
from typing import List, Set
from classFile import *
#Param Butani
#find total deforestation
def totalDeforestation(years:list[deforestationYear]) -> dict:
    total = {}
    for x in years:
        total[x.year] = x.amz
    return total
#Param Butani
#checks if deforestation is greater than a given value
def isHighDeforestation(year:deforestationYear, x:int)->bool:
    return year.amz > x
#Param Butani
#compares deforestation of two years
def compareYears(x:deforestationYear, y:deforestationYear)->str:
    difference = x.amz - y.amz
    if difference > 0:
        return f"Increase of {difference} km^2"
    elif difference < 0:
        return f"Decrease of {abs(difference)} km^2"
    else:
        return "No change"
#Param Butani
#Mentions if deforestation is greater than 10,000 or 5,000 or less than 5,000 in a given year using
#high, moderate, and low; respectively
def sustainabilityMessage(year:deforestationYear)->str:
    if year.amz > 10000:
        return "High deforestation year"
    elif year.amz > 5000:
        return "Moderate deforestation level"
    else:
        return "Low deforestation level"
#Param Butani
#asses the risk level of deforestation
def riskLevel(years: list[deforestationYear]) -> dict[int, str]:
    levels: dict[int, str] = {}
    for y in years:
        if y.amz > 12000:
            levels[y.year] = "SEVERE"
        elif y.amz > 8000:
            levels[y.year] = "HIGH"
        elif y.amz > 4000:
            levels[y.year] = "MODERATE"
        else:
            levels[y.year] = "LOW"

    return levels
#Param Butani
#grabs the year of an object foe use in the function yearOverYearChange
def getYear(obj: deforestationYear):
        return obj.year
#Param Butani
#finds the change of a given variable over the course of a set amount of years
def yearOverYearChange(years: list[deforestationYear],value: str = "amz") -> dict[int, float]:

    sort = sorted(years, key=getYear)

    changes: dict[int, float] = {}

    for i in range(1, len(sort)):
        previous = sort[i - 1]
        current = sort[i]

        prev = getattr(previous, value)
        curr = getattr(current, value)

        changes[current.year] = curr - prev

    return changes
#Param Butani
#finds the total fires of a state
def totalFiresByState(record: List[amazonFires]) -> dict[str, int]:

    total: dict[str, int] = {}
    for x in record:
        if not x.state or x.firespots is None:
            continue
        try:
            state = x.state.strip()
            fires = int(x.firespots)
        except (TypeError, ValueError):
            continue
        total[state] = total.get(state, 0) + fires

    return total

#Jorge Sanchez
#collects total fire spots per year from the records and returns a sorted list of
#years where the total exceeds the given threshold.
def find_years_with_total_above(records: List["amazonFires"], threshold: int) -> List[int]:
    totals_by_year: dict[int, int] = {}

    for r in records:
        if getattr(r, "year", None) is None or getattr(r, "firespots", None) is None:
            continue
        try:
            year = int(r.year)
            fires = int(r.firespots)
        except (TypeError, ValueError):
            continue
        totals_by_year[year] = totals_by_year.get(year, 0) + fires

    years = [yr for yr, total in totals_by_year.items() if total > threshold]
    return sorted(years)
#Jorge Sanchez
#Returns a sorted list of unique state names whose fire records fall within
#the specified latitude and longitude bounding box.
def within_area(records: List["amazonFires"],long1: float,long2: float,lat1: float,lat2: float) -> List[str]:
    min_long, max_long = (long1, long2) if long1 <= long2 else (long2, long1)
    min_lat, max_lat = (lat1, lat2) if lat1 <= lat2 else (lat2, lat1)

    states_in_box: Set[str] = set()

    for r in records:
        if getattr(r, "longitude", None) is None or getattr(r, "latitude", None) is None:
            continue
        if not getattr(r, "state", None):
            continue
        try:
            lon = float(r.longitude)
            lat = float(r.latitude)
        except (TypeError, ValueError):
            continue

        if min_long <= lon <= max_long and min_lat <= lat <= max_lat:
            states_in_box.add(r.state.strip())

    return sorted(states_in_box)
#Jorge Sanchez
#Checks whether a given year falls within the event’s start and end range
#returning False for invalid or missing values.
def i_include_year(self, year: int) -> bool:
        if year is None:
            return False
        try:
            y = int(year)
        except (TypeError, ValueError):
            return False
        if self.start is None or self.end is None:
            return False
        return int(self.start) <= y <= int(self.end)

#Jorge Sanchez
#Calculates the length of the event in years and
#raises an error if the date range is invalid or incomplete.
def duration(self, inclusive: bool = True) -> int:
        if self.start is None or self.end is None:
            raise ValueError("Start and end years must be set")

        start_year = int(self.start)
        end_year = int(self.end)

        if end_year < start_year:
            raise ValueError(f"Invalid event range: {start_year} to {end_year}")

        diff = end_year - start_year
        return diff + 1 if inclusive else diff