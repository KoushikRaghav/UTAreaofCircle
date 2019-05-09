import unittest
import areacircle

class knownvalues(unittest.TestCase):
	def test_area(self):
		result = areacircle.areaofcircle(10)
		expected = 314.1592653589793
		self.assertEqual(expected,result)
	def test_area1(self):
		result = areacircle.areaofcircle(12)
		expected = 452.3893421169302
		self.assertEqual(expected,result)	

if __name__ == '__main__':
	unittest.main()