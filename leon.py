from mamifero import Mamifero

class Leon(Mamifero):
    def __init__(self):
        print("El león es un animal")
        super().__init__("Simba")


obj_leon = Leon()
