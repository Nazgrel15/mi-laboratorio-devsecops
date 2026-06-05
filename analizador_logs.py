import json

print("=========================================")
print("   ANALIZADOR DE SEGURIDAD DE LOGS CLOUD ")
print("=========================================")

archivo_log = "aws_access_log.json"

# Cargamos y leemos el archivo JSON
with open(archivo_log, "r") as archivo:
    eventos = json.load(archivo)

intentos_fallidos_root = 0
ips_atacantes = set()

for evento in eventos:
    # Analizamos las condiciones de riesgo
    if evento["usuario"] == "root" and "FAILED" in evento["resultado"]:
        intentos_fallidos_root += 1
        ips_atacantes.add(evento["ip_origen"])
        print(f"[!] ALERTA: Intento de acceso no autorizado al usuario 'root' desde la IP {evento['ip_origen']} a las {evento['timestamp']}.")
print("=========================================")
# Logica de detección de Fuerza Bruta (más de 1 intento al hilo)
if intentos_fallidos_root >= 2:
    print(f"[🛑 ALERTA CRÍTICA] SE DETECTÓ UN ATAQUE DE FUERZA BRUTA EN CURSO.")
    print(f"    --> Total intentos bloqueados: {intentos_fallidos_root}")
    print(f"    --> IPs sospechosas para banear en el Firewall: {list(ips_atacantes)}")
else:
    print("[✓] Monitoreo normal. No se detectan patrones de ataque.")
print("=========================================")