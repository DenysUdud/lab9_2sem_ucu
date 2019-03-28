# module with tests for class Department.
from class_lab.department import Department

# creating location
loc_1 = Location(8, "BA")
assert ("Room 8. Department: BA" == str(loc_1))
assert (8 == loc_1.get_room())
assert (loc_1.get_department == "BA")

# creating employees

emp_1 = Salaried_emp("Denis", "Shevchenka", "06.09.2001", "head", 120000)
emp_2 = Hourly_emp("Viktor", "Stryiska", "24.04.2001", "analyst", 12, 180)

assert(isinstance(emp_1, Employee))
assert(isinstance(emp_2, Employee))
assert(emp_1.name == "Denis")
assert("Shevchenka" == emp_1.address)
assert("06.09.2001" == emp_1.birthday)
assert("manager" == emp_1.position)
assert(120000 == emp_1.salary)
assert(12 == emp_2.worked_h)
assert(180 == emp_2.salary_p_h)
assert((str(emp_1) == "Salaried_emp<Denis lives in Shevchenka street. Position: manager. Birthday: 06.09.2001. Salary per month: $30000"))
assert((str(emp_1) == "Hourly_emp<Viktor lives in Stryiska street. Position: analyst. Birthday: 24.04.2001. Salary per hour: $180. Worked hours per day: $1000"))

employee_list = (emp_1, emp_2)

dep_1 = Department("BA", "Denis", loc_1, employee_list)
# workers should be in tuple
assert(isinstance(dep_1.workers, tuple))
# location must be instance of Location class
assert(isinstance(dep_1.location, Location))
assert (dep_1.get_location() == "Room 8. Department: BA")
assert (dep_1.sum_salary() == 60000)
assert (dep_1.get_inf_workers() == "Denis lives in Shevchenka street. Position: manager. Birthday: 06.09.2001. Salary per month: $30000\nHourly_emp<Viktor lives in Stryiska street. Position: analyst. Birthday: 24.04.2001. Salary per hour: $180. Worked hours per day: $1000")

