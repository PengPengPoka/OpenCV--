"""
Sebelum kita memasuki teknik pengolahan gambar,
kita perlu memahami dulu

apa

itu

gambar?

menurut alkitab Digital Image Processing karya Rafael C. Gonzalez,
suatu gambar merupakan sebuah fungsi f(x,y) dimana x dan y adalah suatu koordinat bidang (spatial plane)
dan amplitudo f pada titik (x,y) adalah suatu nilai intensitas atau yang biasa kita sebut sebagai gray level.

Pasti diantara kalian ada yang berfikir,
Apa maksud digital dalam digital image processing atau pengolahan citra digital?

Sebelum saya menjawab hal itu, izinkan saya memberi anda satu pertanyaan,
Lu lulus kelas sistem digital kagak si blok?

Baiklah, setelah anda dapat menjawab pertanyaan saya, izinkan saya menjawab pertanyaan anda,
Arti digital dalam pengolahan citra digital adalah dimana nilai f, x, dan y adalah nilai diskrit dan terbatas

mengapa demikian?
karena komputer hanya dapat membaca nilai 0 dan 1, YA HANYA ITU SAJA
maka dari itu, untuk dapat membaca sebuah nilai yang terkandung dalam gambar 
"""

import cv2 as cv  
import os

from matplotlib import pyplot as plt

def main():     
    directory = os.getcwd()
    image_data = directory + "\\utils\\Lenna.png"

    image = cv.imread(image_data)


    cv.imshow("lenna", image)
    key = cv.waitKey()

    if key == ord('c'):     # press c
        exit()  # exit program

    elif key == ord('h'):   # press h
        b, g, r = cv.split(image)

        blue_histogram = cv.calcHist([b], [0], None, [256],[0,256])
        green_histogram = cv.calcHist([g], [0], None, [256],[0,256])
        red_histogram = cv.calcHist([r], [0], None, [256],[0,256])

        plt.plot(blue_histogram, color='blue')
        plt.plot(green_histogram, color='green')
        plt.plot(red_histogram, color='red')
        plt.xlabel("Pixel intensity")
        plt.ylabel("Frequency")
        plt.title("Intensity of image")
        plt.legend(['blue', 'green', 'red'])
        plt.show()

    elif key == ord('g'):   # press g
        grayscale = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

        gray_histogram = cv.calcHist([grayscale], [0], None, [256], [0,256])

        plt.plot(gray_histogram)
        plt.xlabel("Pixel intensity")
        plt.ylabel("Frequency")
        plt.title("Intensity of image")

        cv.imshow("grayscale",grayscale)

        plt.show()
        cv.waitKey(0)

    elif key == ord('b'):   # press b
        grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        ret, threshold = cv.threshold(grayscale, 120, 255, cv.THRESH_BINARY)
        cv.imshow("binary", threshold)
        cv.waitKey(0)

if __name__ == "__main__":
    main()