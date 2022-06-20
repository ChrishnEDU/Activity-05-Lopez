import cv2 as cv
import numpy as np

def exe():
    load()

def load():
    #----Image Load
    ina = cv.imread("ina.jpg")
    #----Getting Color Channel
    check = ina.shape
    #----Checking Colored & Grayscale Load Image
    if check[2] == 3:
        put(ina)
    elif check[2] >= 2:
        print("Image is Grayscale, System Terminated.")
        exit

def put(ina):
    #----User Input for Pixel Values
    print("User Input")
    x = int(input("X Coordinate: "))
    y = int(input("Y Coordinate: "))
    #----Color Channel Input Check
    while True:
        c = int(input("Color Channel: "))
        if c <= 2:
            pixmod(ina,x,y,c)
            break
        else:
            print("Invalid Color Index: | Blue = 0 | Green = 1 | Red = 2 |")

def pixmod(ina,x,y,c):
    #----Color Tag
    if c == 0:
        col = "Blue"
    elif c == 1:
        col = "Green"
    elif c == 2:
        col = "Red"

    #----Output of Pixel Value using item()method
    pix = ina.item(x,y,c)
    print("\nPixel",col,"Value")
    print("Value:",pix)

    #----Before Image Pixel Modify
    pixel = ina[x,y]
    print("\n           Blue | Green | Red")
    print("Before Value:",pixel)
    #----Show Before
    cv.imshow("Before",ina)
    cv.waitKey(0)
    cv.destroyAllWindows()
    #----After Image Pixel Modify
    ina.itemset((x,y,c), 100)
    modpixel = ina[x,y]
    print("After Value: ",modpixel)
    #----Show After
    cv.imshow("After",ina)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    imagedime(ina)

def imagedime(ina):
    inadime = ina.shape

    #----Checking Image Dimension
    x = 500
    y = 500

    if inadime[0] <= x and inadime[1] <= y:
        res = "WITHIN BOUNDARY"
    else:
        res = "NOT IN BOUNDARY"

    print("\nImage Dimension")
    print("Loaded:  ",inadime[0],"x",inadime[1])
    print("Default: ",y,"x",x)
    print("Result:  ",res)
    totpix(ina)
    
def totpix(ina):
    fixreq = 360000 
    tot = len(ina[0]) * len(ina)
    print("\nPixel Count")
    if fixreq == tot:
        de = "NORMAL"
    elif fixreq > tot:
        de = "LOWER"
    else:
        de = "HIGHER"
    print("Loaded:  ",tot)
    print("Default: ",fixreq)
    print("Result:  ",de)
    imgdatype(ina)
    
def imgdatype(ina):
    datatype = ina.dtype
    print("\nImage Data Type")
    print("Type:    ",datatype)

exe()
