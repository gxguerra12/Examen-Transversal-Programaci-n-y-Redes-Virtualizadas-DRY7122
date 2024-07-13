# Script para verificar si un número de VLAN pertenece al rango normal o extendido

def verificar_vlan(numero_vlan):
    numero_vlan = int(numero_vlan)  # Convertir a entero si es necesario

    if 1 <= numero_vlan <= 1000:
        print(f"La VLAN {numero_vlan} pertenece al rango normal.")
    elif 1002 <= numero_vlan <= 4094:
        print(f"La VLAN {numero_vlan} pertenece al rango extendido.")
    else:
        print(f"El número de VLAN {numero_vlan} no es válido.")

# Solicitar al usuario que ingrese el número de VLAN
numero_vlan = input("Ingrese el número de VLAN: ")

# Llamar a la función para verificar la VLAN ingresada
verificar_vlan(numero_vlan)
