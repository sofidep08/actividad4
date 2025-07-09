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

# Programa principal
farmacia = Farmacia()
opcion = ""

while opcion != "7":
    print("\n[4] Agregar medicamentos")
    print("[5] Entregar medicamentos")
    print("[6] Mostrar medicamentos")
    print("[7] Salir")
    opcion = input("Elija una opción: ")

    if opcion == "4":
        medicamento = input("Ingrese el nombre del medicamento: ")
        dosis = input("Ingrese la dosis del medicamento: ")
        farmacia.agregar_medicamento(medicamento, dosis)
    elif opcion == "5":
        farmacia.entregar_medicamento()
    elif opcion == "6":
        farmacia.mostrar_pila()
    elif opcion == "7":
        print("Saliendo...")
    else:
        print("Opción no válida.")
