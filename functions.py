import data
from classFile import deforestationYear
from typing import List, Set

def totalDeforestation(years:list[deforestationYear]) -> dict:
    total = {}
    for x in years:
        total[x.year] = x.amz
    return total

def isHighDeforestation(year:deforestationYear, x:int)->bool:
    return year.amz > x

def compareYears(x:deforestationYear, y:deforestationYear)->str:
    difference = x.amz - y.amz
    if difference > 0:
        return f"Increase of {difference} km^2"
    elif difference < 0:
        return f"Decrease of {abs(difference)} km^2"
    else:
        return "No change"

def sustainabilityMessage(year:deforestationYear)->str:
    if year.amz > 10000:
        return "High deforestation year"
    elif year.amz > 5000:
        return "Moderate deforestation level"
    else:
        return "Low deforestation level"


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

def duration(self, inclusive: bool = True) -> int:
        if self.start is None or self.end is None:
            raise ValueError("Start and end years must be set")

        start_year = int(self.start)
        end_year = int(self.end)

        if end_year < start_year:
            raise ValueError(f"Invalid event range: {start_year} to {end_year}")

        diff = end_year - start_year
        return diff + 1 if inclusive else diff