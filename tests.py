import unittest
from classFile import deforestationYear
from functions import (totalDeforestation, isHighDeforestation, compareYears,sustainabilityMessage)


class TestDeforestationFunctions(unittest.TestCase):

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

    def test2TotalDeforestation(self):
        years = []
        result = totalDeforestation(years)
        self.assertEqual(result, {})

    def test1HighDeforestation(self):
        y = deforestationYear(2004, 100.0, 12001.0)
        result = isHighDeforestation(y, 10000)
        self.assertTrue(result)

    def test2HighDeforestation(self):
        y = deforestationYear(2004, 100.0, 10000.0)
        result = isHighDeforestation(y, 10000)
        self.assertFalse(result)

    def test1CompareYears(self):
        a = deforestationYear(2005, 0.0, 1500.0)
        b = deforestationYear(2004, 0.0, 1200.0)
        result = compareYears(a, b)
        self.assertEqual(result, "Increase of 300.0 km^2")

    def test2CompareYears(self):
        a = deforestationYear(2004, 0.0, 1200.0)
        b = deforestationYear(2005, 0.0, 1500.0)
        result = compareYears(a, b)
        self.assertEqual(result, "Decrease of 300.0 km^2")

    def test1SustainabilityMessage(self):
        y = deforestationYear(2010, 0.0, 15000.0)
        result = sustainabilityMessage(y)
        self.assertEqual(result, "High deforestation year")

    def test2SustainabilityMessage(self):
        y = deforestationYear(2010, 0.0, 7000.0)
        result = sustainabilityMessage(y)
        self.assertEqual(result, "Moderate deforestation level")

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

    def test1getYear(self):
        y = deforestationYear(2004, 0.0, 1000.0)
        result = getYear(y)
        self.assertEqual(result, 2004)

    def test2getYear(self):
        y = deforestationYear(2019, 0.0, 2000.0)
        result = getYear(y)
        self.assertEqual(result, 2019)

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


if __name__ == "__main__":
    unittest.main()