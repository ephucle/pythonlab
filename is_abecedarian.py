import unittest
def is_abecedarian(string):
	sorted_string_list = sorted(string)
	sorted_string = "".join(sorted_string_list)
	if string == sorted_string:
		return True
	else:
		return False


class MyTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(is_abecedarian("abc"), True)
	def test2(self):
		self.assertEqual(is_abecedarian("adc"), False)
	def test3(self):
		self.assertEqual(is_abecedarian("abbcd"), True)
	def test4(self):
		self.assertEqual(is_abecedarian("zabc"), False)


if __name__ == '__main__':
	unittest.main()