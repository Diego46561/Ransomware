# Simulador de Ransomware

Este pequeño proyecto lo desarrolle con ayuda de la IA, la cual simula un ataque de ransomware cifrando cualquier tipo de archivo en base64. 

## Descripción

Este proyecto es una simulación de ransomware con fines educativos y de investigación en ciberseguridad. Permite demostrar el funcionamiento básico del cifrado de archivos y la generación de claves para su recuperación. No debe ser utilizado con fines malintencionados.

## Características

* Cifra archivos en un directorio especificado.
* Genera una clave de cifrado que se debe almacenar de forma segura.
* Opción para descifrar los archivos con la clave correcta.
* Implementado en Python para facilitar su uso y modificación.

## Requisitos

* Python 3.x
* Librerías necesarias (instalar con pip install -r requirements.txt)

## Instalación

1. Clona este repositorio:
```
  git clone https://github.com/tu_usuario/simulador-ransomware.git
```

![Ransomware](https://github.com/user-attachments/assets/451f7f3b-4a5c-4a79-849a-246146a45b30)



2. Accede al directorio del proyecto:  
```
cd simulador-ransomware
```

3. Instala las dependencias necesarias:
```
pip install -r requirements.txt
```

## Uso

### Cifrado de archivos

Ejecuta el siguiente comando para cifrar los archivos del directorio documentos:
```
python cifrar_ransomware.py
```
### Descifrado de archivos

Si tienes la clave correcta, puedes descifrar los archivos:
```
python descifrar_ransomware.py
```
Utiliza la clave `EDUCACION2025`

## Advertencia

Este proyecto es solo para fines educativos y de investigación en ciberseguridad. El uso indebido de este software puede tener consecuencias legales. El autor no se hace responsable de cualquier uso malintencionado.
