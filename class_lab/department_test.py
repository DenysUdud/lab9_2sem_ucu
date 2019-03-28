from class_lab.department import *

print("\nTesting department.py")
print("-------------------------------------------------")

a1 = Hourly_emp("Vika", "Lviv", "12.12.1990", "Director", 30, 10)
a2 = Hourly_emp("Vlad", "Lviv", "01.11.1995", "Printer", 20, 9)
a3 = Salaried_emp("Ulya", "Irshava", "24.05.1978", "Cleaner", 100)

depart = Department("Store", "Mr. Wachevski", "016b", [a1, a2, a3])

assert depart.name == "Store", "Invalid department name"
assert depart.head == "Mr. Wachevski", "Invalid department head"
assert isinstance(depart.room, Location), "depart.room is not a class"

for i in depart.workers:
    assert isinstance(i, Hourly_emp) or isinstance(i, Salaried_emp), "i in depart.workers is not class"

assert depart.salary() == 580, "Invalid total salary"
# .salary() is my name, yours can be different
assert isinstance(a1, Employee) and isinstance(a2, Employee) and isinstance(a3,
                                                                            Employee), "Hourly_emp or Employee_emp is not subclasses of Employee"

assert a1.name == "Vika", "Invalid a1 name"
assert a3.name == "Ulya", "Invalid a3 name"
assert depart.name == depart.room.name, "Invalid room name"
assert depart.room.number == "016b", "Invalid room number"

print("-------------------------------------------------")
print("Passed! ☻")
