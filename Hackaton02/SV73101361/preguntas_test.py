import subprocess
import os

# Definir el directorio de los archivos
directorio = "./Hackaton02/SV73101361/"

# Lista de archivos a probar
archivos = [
    "pregunta1.psc", "pregunta2.psc", "pregunta3.psc", "pregunta4.psc",
    "pregunta5.psc", "pregunta6.psc", "pregunta7.psc", "pregunta8.psc",
    "pregunta9.psc", "pregunta10.psc", "pregunta11.psc", "pregunta12.psc",
    "pregunta13.psc", "pregunta14.psc", "pregunta15.psc", "pregunta16.psc",
    "pregunta17.psc", "pregunta18.psc", "pregunta19.psc", "pregunta20.psc",
    "pregunta21.psc", "pregunta22.psc", "pregunta23.psc", "pregunta24.psc",
    "pregunta25.psc", "pregunta26.psc", "pregunta27.psc", "pregunta28.psc",
    "pregunta29.psc", "pregunta30.psc", "pregunta31.psc", "pregunta32.psc",
    "pregunta33.psc", "pregunta34.psc", "pregunta35.psc", "pregunta36.psc",
    "pregunta37.psc", "pregunta38.psc", "pregunta39.psc", "pregunta40.psc"
]

# Definir los casos de prueba esperados para cada archivo
casos_de_prueba = {
    "pregunta1.psc": [((5, 3), "5")],
    "pregunta2.psc": [((3, 4), "7")],
    "pregunta3.psc": [((6, 6), "36")],
    "pregunta4.psc": [(5, "Impar")],
    "pregunta5.psc": [(15, "El estudiante aprobó con un promedio de: 15.0")],
    "pregunta6.psc": [(41, "865")],
    "pregunta7.psc": [('A', "10%"), ('B', "15%"), ('C', "20%")],
    "pregunta8.psc": [((15, 10), "5")],
    "pregunta9.psc": [(7, "Primo"), (4, "No Primo")],
    "pregunta10.psc": [((8, 9), "17")],
    "pregunta11.psc": [((5, 5, 5), "Los 3 numeros son iguales"), ((8, 3, 5), "El mayor es el numero 1")],
    "pregunta12.psc": [((5, 3), "El mayor es el numero 1"), ((2, 9), "El mayor es el numero 2")],
    "pregunta13.psc": [('a', "Ingresaste la vocal A"), ('b', "No es una vocal")],
    "pregunta14.psc": [(7, "Primo"), (9, "No Primo")],
    "pregunta15.psc": [((15, 8), "15")],
    "pregunta16.psc": [(20, "Descuento aplicado: 0.20")],
    "pregunta17.psc": [((2, 3), "6")],
    "pregunta18.psc": [((10, 2), "20")],
    "pregunta19.psc": [(9, "Primo"), (4, "No Primo")],
    "pregunta20.psc": [(30, "40%")],
    "pregunta21.psc": [((2, 3), "5")],
    "pregunta22.psc": [(4, "Par")],
    "pregunta23.psc": [((6, 2), "12")],
    "pregunta24.psc": [((7, 3), "21")],
    "pregunta25.psc": [(9, "Impar")],
    "pregunta26.psc": [((8, 4), "2")],
    "pregunta27.psc": [((5, 5), "Iguales")],
    "pregunta28.psc": [((6, 2), "6 es mayor")],
    "pregunta29.psc": [(10, "Menor que 10")],
    "pregunta30.psc": [((15, 5), "Multiplo")],
    "pregunta31.psc": [(3, "Numero impar")],
    "pregunta32.psc": [(4, "Numero par")],
    "pregunta33.psc": [((6, 6), "36")],
    "pregunta34.psc": [(10, "Menor que 20")],
    "pregunta35.psc": [((5, 3), "2")],
    "pregunta36.psc": [((9, 3), "Multiplo de 3")],
    "pregunta37.psc": [(11, "Numero primo")],
    "pregunta38.psc": [(12, "Numero compuesto")],
    "pregunta39.psc": [(15, "Numero positivo")],
    "pregunta40.psc": [((4, 2), "4 es mayor")]
}

# Función para ejecutar PSeInt desde la línea de comandos
def ejecutar_pseint(archivo, entrada):
    comando = f"pseint {archivo}"
    resultado = subprocess.run(comando, input=entrada, text=True, capture_output=True, shell=True)
    return resultado.stdout

# Función para realizar pruebas
def realizar_pruebas():
    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        if archivo in casos_de_prueba:
            for entrada, esperado in casos_de_prueba[archivo]:
                # Convertir la entrada a string adecuada para el input
                if isinstance(entrada, tuple):
                    entrada_str = '\n'.join(map(str, entrada))
                else:
                    entrada_str = str(entrada)
                
                salida = ejecutar_pseint(ruta_archivo, entrada_str)
                
                if str(esperado) in salida:
                    print(f"Prueba para {archivo} con entrada {entrada}: PASADA")
                else:
                    print(f"Prueba para {archivo} con entrada {entrada}: FALLIDA")
                    print(f"Salida obtenida: {salida}")
                    print(f"Salida esperada: {esperado}")

# Ejecutar las pruebas
realizar_pruebas()