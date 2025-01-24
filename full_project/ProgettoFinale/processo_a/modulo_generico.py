import cv2
import numpy as np

def interpreta(recv_data):
    if(recv_data == 0):
        print("Nessun oggetto rilevato!")
    else:
        print("Rilevato oggetto!")

def add_disturb(source,dest, noise_ratio):
    image = cv2.imread(source)
    noisy_image = image.copy()
    h,w,c = noisy_image.shape
    noisy_pixels = int(h * w * noise_ratio)
    for _ in range(noisy_pixels):
        row, col = np.random.randint(0, h), np.random.randint(0, w)
        if np.random.rand() < 0.5:
            noisy_image[row, col] = [0, 0, 0] 
        else:
            noisy_image[row, col] = [255, 255, 255]
 
    cv2.imwrite(dest, noisy_image)
