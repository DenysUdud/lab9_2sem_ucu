import unittest
from class_lab.department import Department, Location, Salaried_emp, Hourly_emp


class TestDepartment(unittest.TestCase):
	def setUp(self):
		self.employer_1 = Salaried_emp("Anna", "Ukraine", '21.12.2001',
									   'Director', 2000)
		self.employer_2 = Hourly_emp("John", "London", '14.02.2000', 'Tester',
									 8, 300)
		self.employer_3 = Hourly_emp("Peter", 'USA', '22.05.2001', 'Debugger',
									 7, 250)
		employers = [self.employer_1, self.employer_2, self.employer_3]
		self.test_department = Department('Alpha', 'Johnson', '008', employers)

	def test_init(self):
		self.assertEqual(type(self.employer_2), type(self.employer_3),
						 'Two objects must be of a same class')
		self.assertEqual(self.employer_1.name, "Anna", 'Name is not valid')
		self.assertEqual(self.employer_2.name, "John", 'Name is not valid')
		self.assertEqual(self.employer_3.name, "Peter", 'Name is not valid')
		self.assertNotEqual(self.employer_1.address, self.employer_2.address,
							'Each employee lives in different countries')
		self.assertNotEqual(self.employer_1.address, self.employer_3.address,
							'Each employee lives in different countries')
		self.assertNotEqual(self.employer_2.address, self.employer_3.address,
							'Each employee lives in different countries')

	def test_salary(self):
		self.assertEqual(self.test_department.salary(),
						 2000 + 8 * 300 + 250 * 7)


class TestLocation(unittest.TestCase):
	def setUp(self):
		self.test_location = Location('008', 'Alpha')

	def test_init(self):
		self.assertEqual(self.test_location.number, '008', 'Wrong number')
		self.assertEqual(self.test_location.name, 'Alpha', 'Wrong name')


class TestSalaried_emp(unittest.TestCase):
	def setUp(self):
		self.employer_5 = Salaried_emp("George", "China", '17.02.2001',
									   'Freelancer', 3000)

	def test_init(self):
		self.assertEqual(self.employer_5.name, 'George', 'Wrong name')
		self.assertEqual(self.employer_5.birthday, '17.02.2001',
						 'Wrong birthday')
		self.assertEqual(self.employer_5.address, 'China', 'Wrong address')
		self.assertEqual(self.employer_5.qualification, 'Freelancer',
						 'Wrong qualification')
		self.assertEqual(self.employer_5.sal, 3000, 'Wrong salary')


class TestHourly_emp(unittest.TestCase):
	def setUp(self):
		self.employer_6 = Hourly_emp("Vicky", 'Pakistan', '16.02.2000',
									 'Cleaner', 5, 200)

	def test_init(self):
		self.assertEqual(self.employer_6.name, 'Vicky', 'Wrong name')
		#  sal must be total, not per hour!
		self.assertEqual(self.employer_6.pay, 200 * 5,
						 'Wrong salary! It must be total salary, not per hour')
		self.assertEqual(self.employer_6.position, 'Cleaner',
						 'Wrong qualification')
		self.assertEqual(self.employer_6.address, 'Pakistan', 'Wrong address')
		self.assertEqual(self.employer_6.birth, '16.02.2000',
						 'Wrong birthday')
		self.assertEqual(self.employer_6.hours, 5, 'Wrong time')
		self.assertEqual(self.employer_6.hours, 200, 'Wrong hourly wage')
