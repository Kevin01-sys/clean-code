class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


# Creamos dos instancias de Singleton
singleton1 = Singleton(10)
singleton2 = Singleton(20)
singleton3 = Singleton(30)

print(singleton1.value)  # Salida: 10
print(singleton2.value)  # Salida: 10
print(singleton1 is singleton2)  # Salida: True