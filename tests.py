import unittest
from classFile import deforestationYear
from functions import (totalDeforestation, isHighDeforestation, compareYears,sustainabilityMessage)
import functions
from functions import *
from classFile import *

class TestDeforestationFunctions(unittest.TestCase):
    # Param Butani
    def test1TotalDeforestation(self):
        years = [
            deforestationYear(2004, 100.0, 1200.0),
            deforestationYear(2005, 200.0, 1500.0),
            deforestationYear(2006, 300.0, 900.0)
        ]
        result = totalDeforestation(years)
        expected = {
            2004: 1200.0,
            2005: 1500.0,
            2006: 900.0
        }
        self.assertEqual(result, expected)

    # Param Butani
    def test2TotalDeforestation(self):
        years = []
        result = totalDeforestation(years)
        self.assertEqual(result, {})

    # Param Butani
    def test1HighDeforestation(self):
        y = deforestationYear(2004, 100.0, 12001.0)
        result = isHighDeforestation(y, 10000)
        self.assertTrue(result)

    # Param Butani
    def test2HighDeforestation(self):
        y = deforestationYear(2004, 100.0, 10000.0)
        result = isHighDeforestation(y, 10000)
        self.assertFalse(result)

    # Param Butani
    def test1CompareYears(self):
        a = deforestationYear(2005, 0.0, 1500.0)
        b = deforestationYear(2004, 0.0, 1200.0)
        result = compareYears(a, b)
        self.assertEqual(result, "Increase of 300.0 km^2")

    # Param Butani
    def test2CompareYears(self):
        a = deforestationYear(2004, 0.0, 1200.0)
        b = deforestationYear(2005, 0.0, 1500.0)
        result = compareYears(a, b)
        self.assertEqual(result, "Decrease of 300.0 km^2")

    # Param Butani
    def test1SustainabilityMessage(self):
        y = deforestationYear(2010, 0.0, 15000.0)
        result = sustainabilityMessage(y)
        self.assertEqual(result, "High deforestation year")

    # Param Butani
    def test2SustainabilityMessage(self):
        y = deforestationYear(2010, 0.0, 7000.0)
        result = sustainabilityMessage(y)
        self.assertEqual(result, "Moderate deforestation level")

    # Param Butani
    def test1riskLevel(self):
        years = [
            deforestationYear(2004, 0.0, 13000.0),  # SEVERE
            deforestationYear(2005, 0.0, 9000.0),  # HIGH
            deforestationYear(2006, 0.0, 5000.0),  # MODERATE
            deforestationYear(2007, 0.0, 3000.0)  # LOW
        ]
        result = riskLevel(years)
        expected = {
            2004: "SEVERE",
            2005: "HIGH",
            2006: "MODERATE",
            2007: "LOW"
        }

        self.assertEqual(result, expected)

    # Param Butani
    def test2riskLevel(self):
        years = [
            deforestationYear(2010, 0.0, 12000.0),  # HIGH
            deforestationYear(2011, 0.0, 8000.0),  # MODERATE
            deforestationYear(2012, 0.0, 4000.0)  # LOW
        ]
        result = riskLevel(years)
        expected = {
            2010: "HIGH",
            2011: "MODERATE",
            2012: "LOW"
        }

        self.assertEqual(result, expected)

    # Param Butani
    def test1getYear(self):
        y = deforestationYear(2004, 0.0, 1000.0)
        result = getYear(y)
        self.assertEqual(result, 2004)

    # Param Butani
    def test2getYear(self):
        y = deforestationYear(2019, 0.0, 2000.0)
        result = getYear(y)
        self.assertEqual(result, 2019)

    # Param Butani
    def test1yearOverYear(self):
        years = [
            deforestationYear(2006, 10.0, 900.0),
            deforestationYear(2004, 10.0, 1200.0),
            deforestationYear(2005, 10.0, 1500.0)
        ]
        result = yearOverYearChange(years, "amz")
        expected = {
            2005: 300.0,  # 1500 - 1200
            2006: -600.0  # 900 - 1500
        }

        self.assertEqual(result, expected)

    # Param Butani
    def test2yearOverYear(self):
        years = [
            deforestationYear(2004, 100.0, 1200.0),
            deforestationYear(2005, 250.0, 1500.0),
            deforestationYear(2006, 200.0, 900.0)
        ]
        result = yearOverYearChange(years, "area")
        expected = {
            2005: 150.0,  # 250 - 100
            2006: -50.0  # 200 - 250
        }

        self.assertEqual(result, expected)

    # Param Butani
    def test1totalFiresByState(self):
        records = [
            amazonFires(2004, 1, "AM", 0.0, 0.0, 10),
            amazonFires(2004, 2, "AM", 0.0, 0.0, 5),
            amazonFires(2004, 3, "PA", 0.0, 0.0, 20)
        ]
        result = totalFiresByState(records)
        expected = {
            "AM": 15,
            "PA": 20
        }

        self.assertEqual(result, expected)

    # Param Butani
    def test2totalFiresByState(self):
        records = [
            amazonFires(2004, 1, "", 0.0, 0.0, 10),  # Empty state → skip
            amazonFires(2004, 2, "AM", 0.0, 0.0, None),  # None firespots → skip
            amazonFires(2004, 3, "AM", 0.0, 0.0, 7),  # Valid
            amazonFires(2004, 4, " PA ", 0.0, 0.0, 3)  # Valid (trim spaces)
        ]
        result = totalFiresByState(records)
        expected = {
            "AM": 7,
            "PA": 3
        }

        self.assertEqual(result, expected)

    # Jorge Sanchez
    def test_find_years_with_total_above_part_1(self):
        records = [
            amazonFires(2020, 1, "PA", -10.0, -60.0, 10),
            amazonFires(2020, 2, "PA", -10.1, -60.1, 15),
            amazonFires(2021, 1, "AM", -9.0, -59.0, 5),
            amazonFires(2022, 1, "RO", -8.0, -58.0, 30),
        ]
        expected = [2020, 2022]  # 2020 total=25, 2022 total=30
        actual = functions.find_years_with_total_above(records, 20)
        self.assertEqual(expected, actual)

    # Jorge Sanchez
    def test_find_years_with_total_above_part_2(self):
        records = [
            amazonFires(2019, 1, "PA", -10.0, -60.0, 5),
            amazonFires(2019, 2, "PA", -10.1, -60.1, 4),
            amazonFires(2020, 1, "AM", -9.0, -59.0, 3),
        ]
        # totals: 2019 = 9, 2020 = 3
        expected = []
        actual = functions.find_years_with_total_above(records, 10)
        self.assertEqual(expected, actual)

    # Jorge Sanchez
    def test_within_area_part_1(self):
        records = [
            amazonFires(2020, 1, "PA", -10.0, -60.0, 10),
            amazonFires(2020, 1, "AM", -9.0,  -59.0, 5),
            amazonFires(2020, 1, "RO", -10.0, -70.0, 1),   # outside longitude box
            amazonFires(2020, 1, "PA", -10.5, -60.5, 2),   # duplicate state
        ]
        expected = ["AM", "PA"]
        actual = functions.within_area(records, -61, -58, -11, -9)
        self.assertEqual(expected, actual)

    # Jorge Sanchez
    def test_within_area_part_2(self):
        records = [
            amazonFires(2020, 1, "PA", -10.0, -60.0, 10),
            amazonFires(2020, 1, "AM", -9.0, -59.0, 5),
            amazonFires(2020, 1, "RO", -8.0, -58.0, 3),
        ]

        # Bounds intentionally reversed
        expected = ["AM", "PA", "RO"]
        actual = functions.within_area(records, -58.0, -60.0, -8.0, -10.0)
        self.assertEqual(expected, actual)

    # Jorge Sanchez
    def test_i_include_year_part_1(self):
        event = climateEvent(2000, 2005, "El Nino", 3)
        self.assertTrue(functions.i_include_year(event, 2003))
        self.assertTrue(functions.i_include_year(event, 2000))
        self.assertTrue(functions.i_include_year(event, 2005))

    # Jorge Sanchez
    def test_i_include_year_Part_2(self):
        event = climateEvent(2000, 2005, "El Nino", 3)
        self.assertFalse(functions.i_include_year(event, 1999))
        self.assertFalse(functions.i_include_year(event, 2006))
        self.assertFalse(functions.i_include_year(event, None))
        self.assertFalse(functions.i_include_year(event, "bad"))

    # Jorge Sanchez
    def test_duration_normal(self):
        event = climateEvent(2000, 2005, "El Nino", 3)
        self.assertEqual(6, functions.duration(event))
        self.assertEqual(5, functions.duration(event, inclusive=False))

    # Jorge Sanchez
    def test_duration_errors(self):
        event = climateEvent(2010, 2000, "La Nina", 2)
        with self.assertRaises(ValueError):
            functions.duration(event)

if __name__ == "__main__":
    unittest.main()