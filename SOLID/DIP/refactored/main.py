from factory.MySqlEmployeePersistenceFactory import MySqlEmployeePersistenceFactory
from factory.EmployeeMemoryPersistenceFactory import EmployeeMemoryPersistenceFactory
from Company import Company
from Employee import Employee


def main():
    try:
        company = Company(EmployeeMemoryPersistenceFactory())
        company.add_employee(Employee("Kevin Perez", 50000))
        company.add_employee(Employee("Maria Garcia", 60000))

        employees = company.get_employees()
        for employee in employees:
            print("Nombre:", employee.full_name)
            print("Salario:", employee.salary)
            print("------------------------")

    except (ValueError, AttributeError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
