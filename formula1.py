
#algoritmo de la formula 1
class Formula1:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Piloto(Formula1):
    def __init__(self, nombre, edad, equipo, numero):
        super().__init__(nombre, edad)
        self.equipo = equipo
        self.numero = numero

    def info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Equipo: {self.equipo}, Número: {self.numero}"

class Equipo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede
        self.pilotos = []

    def agregar_piloto(self, piloto):
        self.pilotos.append(piloto)

    def listar_pilotos(self):
        return [piloto.info() for piloto in self.pilotos]

equipo_ferrari = Equipo("Ferrari", "Maranello")
piloto_carlos= Piloto("Carlos Sainz", 25, "Ferrari", 55)
piloto_leclerc= Piloto("Charles Leclerc", 24, "Ferrari", 16)


equipo_ferrari.agregar_piloto(piloto_carlos)
equipo_ferrari.agregar_piloto(piloto_leclerc)

equipo_RedBull = Equipo("Red Bull", "Milton Keynes")
piloto_max= Piloto("Max Verstappen", 25, "Red Bull", 1)
piloto_checo = Piloto("Checo Perez", 33, "Red Bull", 11)

equipo_RedBull.agregar_piloto(piloto_max)
equipo_RedBull.agregar_piloto(piloto_checo)

print("\nInformación del Equipo Ferrari:")
print(f"Nombre: {equipo_ferrari.nombre}, Sede: {equipo_ferrari.sede}")
print("Pilotos:")
for piloto_info in equipo_ferrari.listar_pilotos():
    print(piloto_info)

print("\nInformación del Equipo Red Bull:")
print(f"Nombre: {equipo_RedBull.nombre}, Sede: {equipo_RedBull.sede}")
print("Pilotos:")
for piloto_info in equipo_RedBull.listar_pilotos():
    print(piloto_info)    

