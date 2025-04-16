# import unittest

# main_component = {1 : "I", 5 : "V", 10 : "X", 50 : "L"}

# def arabske_na_rimske(ar):
#   if ar == 50:
#     return "L"
#   if ar == 10:
#     return "X"
#   if ar == 5:
#     return "V"
#   if ar == 1:
#     return "I"


# class TestArabskeNaRimske(unittest.TestCase):
#   def test_foo(self):
#     self.assertEqual(1, 1)


# class TestArabskeNaRimske(unittest.TestCase):
#   def test_one(self):
#     self.assertEqual(arabske_na_rimske(1), "I")
  
#   def test_five(self):
#     self.assertEqual(arabske_na_rimske(5), "V")

#   def test_ten(self):
#     self.assertEqual(arabske_na_rimske(10), "X")

#   def test_fifty(self):
#     self.assertEqual(arabske_na_rimske(50), "L")



# po refactoringu:

import unittest

main_components = {1: "I", 5: "V", 10: "X", 50: "L", 20: "XX"}

def arabske_na_rimske(ar):
  return main_components[ar]



class TestArabskeNaRimske(unittest.TestCase):
  def test_main_components(self):
    self.assertEqual(arabske_na_rimske(1), "I")
    self.assertEqual(arabske_na_rimske(5), "V")
    self.assertEqual(arabske_na_rimske(10), "X")
    self.assertEqual(arabske_na_rimske(50), "L")    

  def test_twenty(self):
    self.assertEqual(arabske_na_rimske(20), "XX")
