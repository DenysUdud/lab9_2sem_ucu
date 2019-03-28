class Employee:
		"""
		A class for representing employee.
		"""
		def __init__(self, name, address, birth, position):
			self.name = name
			self.address = address
			self.birth = birth
			self.position = position

class Hourly_emp(Employee):
	"""
	A class for representing hourly paid employee.
	"""
	def __init__(self, name, address, birth, position, hours, pay):
		super().__init__(name, address, birth, position)
		self.pay = pay
		self.hours = hours

class Salaried_emp(Employee):
	"""
	A class for representing months salaried employee.
	"""
	def __init__(self, name, address, birth, position, salary):
		super().__init__(name, address, birth, position)
		self.salary = salary

class Location:
	"""
	A class for representing location.
	"""
	def __init__(self, number, name):
		self.number = number
		self.name = name

class Department:
	"""
	A class for representing department and counting salary.
	"""
	def __init__(self, name, head, number, employees):
		self.name = name
		self.head = head
		self.number = number
		self.room = Location(self.number, self.name)
		self.workers = employees
	def salary(self):
		couter = 0
		for emp in self.workers:
			if isinstance(emp, Hourly_emp):
				couter += emp.hours * emp.pay
			elif isinstance(emp, Salaried_emp):
				couter += emp.salary
		return couter


	


