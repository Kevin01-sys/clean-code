from Dolphin import Dolphin
from CannotWalkException import CannotWalkException


def main():
    dolphin = Dolphin()
    try:
        dolphin.walk()
    except CannotWalkException as e:
        print(e)


if __name__ == "__main__":
    main()
