class MiClase:
    def __call__(self, *args, **kwargs):
        print("Llamando a la instancia de MiClase")

# Crear una instancia de MiClase
objeto = MiClase()

# Llamar a la instancia como si fuera una función
objeto()  # Esto imprimirá "Llamando a la instancia de MiClase"