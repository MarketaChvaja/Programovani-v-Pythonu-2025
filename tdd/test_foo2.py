import unittest

main_components = {1 : "I", 5: "V", 10: "X", 50: "L", 100: "C"}

def arabske_na_rimske(ar):
  if (ar%1) == 0 and (ar//1) in main_components:
    return main_components[ar//1]

  if (ar%2) == 0 and (ar//2) in main_components:
    return main_components[ar//2] + main_components[ar//2]

  if (ar%3) == 0 and (ar//3) in main_components:
    return main_components[ar//3] + main_components[ar//3] + main_components[ar//3]




class TestArabskeNaRimske(unittest.TestCase):
  def test_main_components(self):
    self.assertEqual(arabske_na_rimske(1), "I")
    self.assertEqual(arabske_na_rimske(5), "V")
    self.assertEqual(arabske_na_rimske(10), "X")
    self.assertEqual(arabske_na_rimske(50), "L")
    self.assertEqual(arabske_na_rimske(100), "C")

  def test_two_times(self):
    self.assertEqual(arabske_na_rimske(2), "II")
    self.assertEqual(arabske_na_rimske(20), "XX")
    self.assertEqual(arabske_na_rimske(200), "CC")

  def test_three_times(self):
    self.assertEqual(arabske_na_rimske(3), "III")
    self.assertEqual(arabske_na_rimske(30), "XXX")
    self.assertEqual(arabske_na_rimske(300), "CCC")
