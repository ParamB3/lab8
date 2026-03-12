import csv
import zipfile
from classFile import deforestationYear, amazonFires, climateEvent

#This is credited to ChatGpt
def _open_csv_from_zip(zip_path, member_name):

    #Returns (zipfile_handle, csv_dict_reader)
    #Uses utf-8-sig to handle BOM safely.

    zf = zipfile.ZipFile(zip_path, "r")
    raw = zf.open(member_name, "r")
    text_lines = (line.decode("utf-8-sig") for line in raw)
    reader = csv.DictReader(text_lines)
    return zf, reader

#This is credited to ChatGpt
def load_deforestation_years(zip_path="archive.zip"):
    """
    Reads: def_area_2004_2019.csv
    Returns: list[deforestationYear]
    Uses only these fields:
      - year (int)
      - area (float)  -> "ACRE" column (matches your design doc)
      - amz (float)   -> "AMZ LEGAL" column
    """
    member = "def_area_2004_2019.csv"
    zf, reader = _open_csv_from_zip(zip_path, member)

    years = []
    try:
        for row in reader:
            year_str = row.get("Ano/Estados", "").strip()
            if not year_str:
                continue

            year = int(year_str)

            # Your proposal specifically used ACRE for area (can change if you want another state)
            area = float(row.get("ACRE", "0").strip() or 0)

            # total legal amazon deforestation for that year
            amz_total = float(row.get("AMZ LEGAL", "0").strip() or 0)

            years.append(deforestationYear(year, area, amz_total))
        return years
    finally:
        zf.close()

#This is credited to ChatGpt
def load_fire_records(zip_path="archive.zip"):
    """
    Reads: inpe_brazilian_amazon_fires_1999_2019.csv
    Returns: list[amazonFires]
    """
    member = "inpe_brazilian_amazon_fires_1999_2019.csv"
    zf, reader = _open_csv_from_zip(zip_path, member)

    fires = []
    try:
        for row in reader:
            # some rows may have quotes in values; strip them
            year = int(row["year"].strip().strip('"'))
            month = int(row["month"].strip().strip('"'))
            state = row["state"].strip().strip('"')

            latitude = float(row["latitude"].strip().strip('"'))
            longitude = float(row["longitude"].strip().strip('"'))

            # firespots may appear like "3.0" so use float then int
            firespots = int(float(row["firespots"].strip().strip('"')))

            fires.append(amazonFires(year, month, state, latitude, longitude, firespots))
        return fires
    finally:
        zf.close()

#Param Butani
def loadClimateEvents(zip_path="archive.zip"):
    member = "el_nino_la_nina_1999_2019.csv"
    zf, reader = _open_csv_from_zip(zip_path, member)
    events = []
    try:
        for x in reader:
            start = int(x["start year"].strip())
            end = int(x["end year"].strip())
            event = x["phenomenon"].strip()
            severity = x["severity"].strip()
            events.append(climateEvent(start, end, event, severity))
        return events
    finally:
        zf.close()