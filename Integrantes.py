integrantes = [
    {"nombre": "Alejandro", "apellido": "Allende"},
    {"nombre": "Fernando", "apellido": "Muñoz"},
    {"nombre": "Gamaliel", "apellido": "Guerra"},
]

nombres_apellidos = [f"{integrante['nombre']} {integrante['apellido']}" for integrante in integrantes]

print(nombres_apellidos)
