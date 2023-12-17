import cv2
import numpy as np

for i in range(1, 6):
    imagem = cv2.imread('desmatamento5.png')

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    imagem_binaria = cv2.threshold(imagem_cinza, 10, 255, cv2.THRESH_BINARY)

    menor_limite = np.array([80, 80, 80], dtype=np.uint8)
    maior_limite = np.array([120, 138, 145], dtype=np.uint8)

    mascara = cv2.inRange(imagem, menor_limite, maior_limite)

    mascara_final = cv2.bitwise_and(imagem_binaria, mascara)

    contornos = cv2.findContours(mascara_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    resultado = imagem.copy()
    cv2.drawContours(resultado, contornos, -1, (0, 255, 255), thickness=cv2.FILLED)

    cv2.imwrite('desmatamento5.png', resultado)
