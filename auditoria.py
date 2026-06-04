import os
import platform

print("=========================================")
print("   SISTEMA DE AUDITORÍA LOCAL INICIAL    ")
print("=========================================")
# Detecta el sistema operativo y muestra información relevante
print(f"[+] Sistema Operativo detectado: {platform.system()} {platform.release()}" )

# Muestra la ruta donde se esta ejecutando el script
print(f"[+] Ruta de ejecución: {os.getcwd()}")

# Verifica si tienes variables de entorno criticas configuradas
print("[+] Uusario ejecutando el script: {usuario}")
print("=========================================")