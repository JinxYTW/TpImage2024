
import numpy as np

from matplotlib import pyplot as plt
import cv2 as cv

if __name__ == "__main__":


    #Ouvrir une image
    img = cv.imread("imagesTP/CerisierP.jpg")
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    #Afficher une image
    plt.figure()
    plt.imshow(img)

    #Afficher les canaux
    rouge = img[:,:, 0]
    vert = img[:,:, 1]
    bleu = img[:,:, 2]
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.subplot(2, 2, 2)
    plt.imshow(rouge, cmap="Reds")
    plt.subplot(2, 2, 3)
    plt.imshow(vert, cmap="Greens")
    plt.subplot(2, 2, 4)
    plt.imshow(bleu, cmap="Blues")

    # Transformation en niveau de gris
    imgG = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    plt.figure()
    plt.imshow(imgG, cmap="gray")

    plt.show()

    def histogramme(img):
        hist = np.zeros(256) 
        for i in range(256): 
            hist[i] = np.sum(img == i)
        return hist
    
    hist=histogramme(imgG)
    plt.bar(range(256), hist)
    plt.show()
    
    def histogrammeCumule(hist):
        histCum = np.zeros(256)
        histCum[0] = hist[0]
        for i in range(1, 256):
            histCum[i] = histCum[i-1] + hist[i]
        return histCum
    
    def egalisationHistogramme(img):
        hist = histogramme(img)
        histCum = histogrammeCumule(hist)
        histCum = (histCum - histCum.min()) * 255 / (histCum.max() - histCum.min())
        imgE = histCum[img]
        return imgE
    


