from BasicCalculator import BasicCalculator


def main():
    basic_calculator = BasicCalculator()
    try:
        result = basic_calculator.divide(1,0)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
