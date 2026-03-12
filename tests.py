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

    def test3SustainabilityMessage(self):
        y = deforestationYear(2011, 0.0, 7000.0)
        result = sustainabilityMessage(y)
        self.assertEqual(result, "Moderate deforestation level")


if __name__ == "__main__":
    unittest.main()