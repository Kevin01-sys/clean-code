

class MisMetaclase(type):
    def __new__(cls, name, bases, attrs):
        print("Creando clase:", name)
        return super().__new__(cls, name, bases, attrs)


class MiClase(metaclass=MisMetaclase):
    atributo = 10

    def __init__(self, x):
        self.x = x


def main():
    print("First day")
    #objet = MiClase(5)

if __name__ == "__main__":
    main()
