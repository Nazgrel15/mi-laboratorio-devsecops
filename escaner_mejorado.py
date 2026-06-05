from datetime import datetime 
import os

print("[+] Iniciando análisis de seguridad de código...")

archivo_a_revisar = "config.txt"
palabras_peligrosas = ["SECRET_KEY", "PASSWORD", "CLAVE", "TOKEN"]
hallazgos = []

# 1. Analizar el archivo en busca de fallas
with open(archivo_a_revisar, "r") as archivo:
    for numero_linea, linea in enumerate(archivo, 1):
        for palabra in palabras_peligrosas:
            if palabra in linea.upper():
                # Guardamos los detalles de la falla en una lista
                hallazgos.append({
                    "linea": numero_linea,
                    "tipo": palabra,
                    "contenido": linea.strip()
                })
# 2. Generar el "Artefacto" (Reporte de auditoría) si hay fallas
if hallazgos:
    nombre_reporte = "REPORTE_SEGURIDAD.md"
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(nombre_reporte, "w", encoding="utf-8") as reporte:
        reporte.write("# 🛡️ REPORTE AUTOMATIZADO DE AUDITORÍA DE CÓDIGO\n")
        reporte.write(f"**Fecha de ejecución:** {fecha_actual}\n")
        reporte.write(f"**Archivo analizado:** `{archivo_a_revisar}`\n\n")
        reporte.write("## ⚠️ VULNERABILIDADES DETECTADAS\n")
        reporte.write("Se han encontrado credenciales expuestas en texto plano. **¡Acción requerida inmediata!**\n\n")
        reporte.write("| Línea | Patrón Detectado | Código Sospechoso |\n")
        reporte.write("| :---: | :---: | :--- |\n")

        for h in hallazgos:
            reporte.write(f"| {h['linea']} | `{h['tipo']}` | `{h['contenido']}` |\n")
    print(f"[ALERTA] Análisis finalizado. Se ha generado el archivo '{nombre_reporte}' con los errores.")
else:
    print("[ÉXITO] No se detectaron riesgos. Código limpio.")