import cv2
from pyzbar.pyzbar import decode
import threading
import requests
import tkinter
import time 
import pprint
import pandas as pd
from imprimir import registro_hoy

def dibujar_rectangulo_con_texto(imagen, rectangulo, texto):
    # Obtener las coordenadas del rectángulo
    x, y, w, h = rectangulo

    # Dibujar el rectángulo rojo alrededor del código de barras
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Definir la configuración del texto
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    thickness = 1
    text_size, _ = cv2.getTextSize(texto, font, font_scale, thickness)

    # Calcular la posición del texto
    text_x = x + int((w - text_size[0]) / 2)
    text_y = y - 10

    # Dibujar el texto en la imagen
    cv2.putText(imagen, texto, (text_x, text_y), font, font_scale, (0, 0, 255), thickness)

def leer_codigo_qr(imagen):
    # Decodificar códigos QR
    codigos_qr = decode(imagen)

    # Mostrar contenido de los códigos QR
    for codigo_qr in codigos_qr:
        data = codigo_qr.data.decode('utf-8')
        print(f"Código QR: {data}")
    
    
        
def leer_codigo_barras(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Decodificar códigos de barras
    codigos_barras = decode(imagen_gris)

    # Mostrar contenido de los códigos de barras y dibujar el rectángulo con texto
    for codigo_barras in codigos_barras:
        data = codigo_barras.data.decode('utf-8')
        print(f"Código de barras: {data}")
        dibujar_rectangulo_con_texto(imagen, codigo_barras.rect, f"{data}")
        return data
    
   
def peticion (data):
    url = f'https://404a-190-233-181-4.sa.ngrok.io/kirb_api/main/{data}'
    response = requests.get (url)
    pprint.pprint
    (response.text)
    #time.sleep(1)
    
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
        cod = leer_codigo_barras(imagen)

        if  type(cod) == str:
            peticion (cod)
        

        # Mostrar la imagen con el rectángulo y el texto
        
        cv2.imshow("Lector de códigos", imagen)

    
    
    # Liberar la captura de la cámara y cerrar las ventanas

    captura.release()
    cv2.destroyAllWindows()
    registro_hoy()

