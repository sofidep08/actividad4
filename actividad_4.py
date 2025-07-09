pila = []
class Farmacia:
    def __init__(self,nombre_medicamentos,dosis):
        self.nombre_medicamento = nombre_medicamentos
        self.dosis = dosis
    def agregar_medicamento (self,nombre_medicamento,dosis):
        pila.append((nombre_medicamento,dosis))
        print("Medicamento guardado")
    def entregar_medicamento (self):
        pila.pop(0)
        print("Medicamento entregado")
    def mostrar_pila(self):
        print("Medicamentos guardados")
        print(pila)

    opcion=0
    while opcion != 7:
        print("[4] Agregar medicamentos")
        print("[5] Entregar medicamentos")
        print("[6] Mostrar medicamentos")
        print("[7] salir")
        opcion = input(print("Elija una opcion: "))

        if opcion == "4":
            medicamento = input("Ingrese el nombre del medicamento: ")
            dosiss = input("Ingrese la dosis del medicamento: ")
            agregar_medicamento(medicamento,dosiss)
        elif opcion == "5":
            print("Entregando medicamento.....")
            print()
            entregar_medicamento()
        elif opcion == "6":
            print("Mostrando elementos en la pila")
            mostrar_pila()
        elif opcion == "7":
            print("Saliendo...")