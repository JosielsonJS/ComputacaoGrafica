import cv2
import numpy as np

img = cv2.imread('C:\/Users\/josie\/img-test.PNG')

#print(img.shape)

pontos = np.array([[100+500,50], [200+500, 50], [250+500, 150], [150+500, 200], [50+500, 150]], np.int32)
cv2.polylines(img, [pontos], isClosed=True, color=(0, 255, 0), thickness=2)

cv2.circle(img, [604,339], 20, (255, 255, 255), thickness=2)

cv2.imshow('Imagem com Poligono', img)
cv2.waitKey(0)
cv2.destroyAllWindows()