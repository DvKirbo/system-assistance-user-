import cv2
from pyzbar.pyzbar import decode
import requests
import tkinter


def dibujar_rectangulo(imagen, rectangulo):
    # Obtener las coordenadas del rectángulo
    x, y, w, h = rectangulo

    # Dibujar el rectángulo rojo alrededor del código de barras
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 0, 255), 2)
    

def leer_codigo_qr(imagen):
    # Decodificar códigos QR
    codigos_qr = decode(imagen)

    # Mostrar contenido de los códigos QR
    for codigo_qr in codigos_qr:
        data = codigo_qr.data.decode('utf-8')
        print(f"Código QR: {data}")
        return data

def leer_codigo_barras(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Decodificar códigos de barras
    codigos_barras = decode(imagen_gris)

    # Mostrar contenido de los códigos de barras y dibujar el rectángulo
    for codigo_barras in codigos_barras:
        data = codigo_barras.data.decode('utf-8')
        print(f"Código de barras: {data}")
        dibujar_rectangulo(imagen, codigo_barras.rect)
        return data

if __name__ == "__main__":
    # Capturar video desde la cámara
    captura = cv2.VideoCapture(0)

    while True:
        # Leer la imagen de la cámara
        _, imagen = captura.read()

        # Detectar la tecla ESC para salir del bucle
        if cv2.waitKey(1) == 27:
            break

        # Procesar la imagen y leer los códigos QR y códigos de barras
        leer_codigo_qr(imagen)
        leer_codigo_barras(imagen)

        # Mostrar la imagen con el rectángulo dibujado
        cv2.imshow("Lector de códigos", imagen)

    # Liberar la captura de la cámara y cerrar las ventanas
    captura.release()
    
    
    cv2.destroyAllWindows()
