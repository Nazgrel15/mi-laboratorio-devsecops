print("=========================================")
print("     ESCÁNER DE SEGURIDAD DE CÓDIGO      ")
print("=========================================")

archivo_a_revisar = "config.txt"
palabras_peligrosas = ["SECRET_KEY", "PASSWORD", "CLAVE", "TOKEN"]
vulnerabilidad_detectada = False

# Abrimos y leemos el archivo línea por línea
with open(archivo_a_revisar, "r") as archivo:
    for numero_linea, linea in enumerate(archivo, 1):
        # Revisamos si alguna palabra peligrosa está presente en la línea
        for palabra in palabras_peligrosas:
            if palabra in linea.upper():
                print(f"[ALERTA CRÍTICA] Se encontró un posible secreto expuesto en la línea {numero_linea}!")
                print(f"    --> Texto sospechoso: {linea.strip()}")
                vulnerabilidad_detectada = True
                
print("=========================================")
if vulnerabilidad_detectada:
    print("[RESULTADO] ALERTA: El archivo NO es seguro para subir a GitHub.")
else:
    print("[RESULTADO] ÉXITO: No se detectaron credenciales expuestas.")
print("=========================================")