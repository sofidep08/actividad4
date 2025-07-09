class Paciente:
    def __init__(self, nombre,edad,enfermedad,id):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad
        self.id = id

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, edad: {self.edad}, enfermedad: {self.enfermedad}, id: {self.id}")


cola = []

opcion=0
paciente_encontrado = ""
while opcion != 7:
    print("==clinica==")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. mostrar lista de pacientes")


    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        print("===Registrar paciente===")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        id = input("ID: ")
        enfermedad = input("Enfermedad: ")
        pacientes = Paciente(nombre,edad,enfermedad,id)
        cola.append(pacientes)
    if opcion == 2:
        print("===atender paciente===")
        for paciente in cola:
            paciente_encontrado = paciente
            paciente_encontrado.mostrar_info()
            break
        if paciente_encontrado:
            print("Paciente atendido correctamente")
            cola.remove(paciente_encontrado)
        else:
            print("no hay pacientes.")

    if opcion == 3:
        print("===lista de pacientes===")
        for paciente in cola:
            paciente.mostrar_info()

