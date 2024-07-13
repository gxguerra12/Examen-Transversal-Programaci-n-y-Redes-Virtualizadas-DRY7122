def obtener_distancia_duracion(ciudad_origen, ciudad_destino):
    # Distancias aproximadas entre Santiago de Chile y algunas ciudades de Argentina
    distancias = {
        ('santiago', 'buenos aires'): {'distancia_km': 1150, 'duracion': '1 día'},
        ('santiago', 'mendoza'): {'distancia_km': 360, 'duracion': '5 horas'},
        ('santiago', 'bariloche'): {'distancia_km': 1100, 'duracion': '13 horas'}
    }
    
    # Convertimos las ciudades a minúsculas para ser insensibles a mayúsculas/minúsculas
    ciudad_origen = ciudad_origen.lower()
    ciudad_destino = ciudad_destino.lower()
    
    # Buscamos la distancia y duración aproximada en la base de datos simulada
    clave = (ciudad_origen, ciudad_destino)
    if clave in distancias:
        distancia_km = distancias[clave]['distancia_km']
        duracion = distancias[clave]['duracion']
        distancia_millas = distancia_km * 0.621371  # 1 kilómetro = 0.621371 millas
        return distancia_millas, distancia_km, duracion
    else:
        return None, None, None

def main():
    print("Bienvenido al sistema de cálculo de viaje.")
    while True:
        ciudad_origen = input("Ingrese la ciudad de origen (Santiago) o 's' para salir: ").strip().lower()
        if ciudad_origen == 's':
            print("Saliendo del programa...")
            break

        ciudad_destino = input("Ingrese la ciudad de destino (Buenos Aires, Mendoza, Bariloche) o 's' para salir: ").strip().lower()
        if ciudad_destino == 's':
            print("Saliendo del programa...")
            break
        
        distancia_millas, distancia_km, duracion = obtener_distancia_duracion(ciudad_origen, ciudad_destino)
        
        if distancia_km and duracion:
            print(f"\nLa distancia entre {ciudad_origen.capitalize()} y {ciudad_destino.capitalize()} es:")
            print(f"{distancia_millas:.2f} millas")
            print(f"{distancia_km} kilómetros")
            print(f"La duración estimada del viaje es de {duracion}.")
            
            # Opciones de medio de transporte
            print("\nOpciones de medio de transporte:")
            print("1. Avión")
            print("2. Automóvil")
            print("3. Autobús")
            opcion = input("Seleccione el medio de transporte (1/2/3): ").strip()
            
            if opcion == '1':
                medio_transportacion = "avión"
            elif opcion == '2':
                medio_transportacion = "automóvil"
            elif opcion == '3':
                medio_transportacion = "autobús"
            else:
                print("Opción no válida. Intente de nuevo.")
                continue
            
            # Narrativa del viaje basado en el medio de transporte elegido
            print(f"\nNarrativa del viaje desde {ciudad_origen.capitalize()} a {ciudad_destino.capitalize()} en {medio_transportacion}:")
            print(f"Viajarás desde {ciudad_origen.capitalize()} a {ciudad_destino.capitalize()} en {medio_transportacion}.")
            print(f"Llegarás después de {duracion} de viaje.")
        
        else:
            print("No se pudo obtener la información para las ciudades ingresadas. Inténtelo de nuevo.")
        
        print("\n---\n")

if __name__ == "__main__":
    main()

