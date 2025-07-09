class Paciente:
    def __init__(self, nombre,edad,enfermedad,id):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad
        self.id = id

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, edad: {self.edad}, enfermedad: {self.enfermedad}, id: {self.id}")

class Farmacia:
    def __init__(self):
        self.pila = []

    def agregar_medicamento(self, medicamento, dosis):
        self.pila.append((medicamento, dosis))
        print("Medicamento guardado")

    def entregar_medicamento(self):
        if self.pila:
            medicamento = self.pila.pop()  # LIFO
            print(f"Medicamento entregado: {medicamento[0]}, Dosis: {medicamento[1]}")
        else:
            print("No hay medicamentos para entregar.")

    def mostrar_pila(self):
        if self.pila:
            print("Medicamentos guardados:")
            for med in reversed(self.pila):
                print(f"- {med[0]} ({med[1]})")
        else:
            print("No hay medicamentos en la pila.")
cola = []
farmacia = Farmacia()
opcion = ""
opcion=0
paciente_encontrado = ""
while opcion != 7:
    print("==clinica==")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. mostrar lista de pacientes")
    print("4. Agregar medicamentos")
    print("5. Entregar medicamentos")
    print("6. Mostrar medicamentos")
    print("7. Salir")


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

    if opcion == 4:
        medicamento = input("Ingrese el nombre del medicamento: ")
        dosis = input("Ingrese la dosis del medicamento: ")
        farmacia.agregar_medicamento(medicamento, dosis)
    elif opcion == 5:
        farmacia.entregar_medicamento()
    elif opcion == 6:
        farmacia.mostrar_pila()
    elif opcion == 7:
        print("Saliendo...")
    else:
        print("Opción no válida.")
