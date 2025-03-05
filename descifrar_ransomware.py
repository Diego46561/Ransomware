import os
import base64

CARPETA_ORIGINAL = os.path.expanduser("~/Documents")

def simular_descifrado_carpeta():
    clave_correcta = "EDUCACION2025"
    clave_usuario = input("Ingresa la clave para recuperar tus archivos: ")
    
    if clave_usuario == clave_correcta:
        for root, _, files in os.walk(CARPETA_ORIGINAL):
            for archivo in files:
                if archivo.endswith(".lockout"):
                    ruta_cifrada = os.path.join(root, archivo)
                    ruta_restaurada = os.path.join(root, archivo.replace(".lockout", ""))
                    try:
                        with open(ruta_cifrada, "r") as f:
                            contenido_descifrado = base64.b64decode(f.read())
                        with open(ruta_restaurada, "wb") as f:
                            f.write(contenido_descifrado)
                        os.remove(ruta_cifrada)
                    except Exception as e:
                        print(f"Error al procesar {archivo}: {e}")
        print(f"¡Archivos restaurados en '{CARPETA_ORIGINAL}' y subcarpetas!")
    else:
        print("Clave incorrecta.")

if __name__ == "__main__":
    simular_descifrado_carpeta()
