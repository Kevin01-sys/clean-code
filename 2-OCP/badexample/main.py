from Company import Company
from Programmer import Programmer


def main():
    company = Company()
    company.add_programmer("Kevin Perez", 50000)
    company.add_programmer("Maria Garcia", 60000)

    programmers = company.get_programmers()
    for programmer in programmers:
        print("Nombre:", programmer.get_full_name())
        print("Salario:", programmer.get_salary())
        print("------------------------")


if __name__ == "__main__":
    main()
