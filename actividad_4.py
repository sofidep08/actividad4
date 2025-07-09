class Paciente:
    def __init__(self, nombre,edad,enfermedad,id):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad
        self.id = id



from queue import Queue

cola = Queue()

opcion=0
while opcion != 7:
    print("==clinica==")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. mostrar cola de pacientes")
    print("4. Agrgar medicamento")
    print("5. entregar medicamento")
    print("6. mostrar medicamentos")
    print("7. Salir")

    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        print("Registrar paciente")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        id = input("ID: ")
        enfermedad = input("Enfermedad: ")
        pacientes = Paciente(nombre,edad,enfermedad,id)
        cola.put(pacientes)
    if opcion == 2:
        print("atender paciente")
        nombrebuscar = input("Nombre: ")

