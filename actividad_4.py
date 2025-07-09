pila = []
class Farmacia:
    def __init__(self,nombre_medicamentos,dosis):
        self.nombre_medicamento = nombre_medicamentos
        self.dosis = dosis
    def agregar_medicamento (self,nombre_medicamento,dosis):
        pila.append((nombre_medicamento,dosis))
        print("Medicamento guardado")

