from Company import Company
from Programmer import Programmer
from Manager import Manager


def main():
    company = Company()
    company.add_employee(Programmer("Kevin Perez", 50000))
    company.add_employee(Programmer("Maria Garcia", 60000))
    company.add_employee(Manager("Pepito Marm", 70000, 10000))

    programmers = company.get_employees()
    for programmer in programmers:
        print("Nombre:", programmer.get_full_name())
        print("Salario:", programmer.get_salary())
        print("------------------------")


if __name__ == "__main__":
    main()
