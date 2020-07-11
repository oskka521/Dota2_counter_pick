import numpy as np
import cv2
from PIL import ImageGrab
import time
import os


def convert_to_gray(img):
    processed_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return(processed_img)


def extract_image():
    #print_screen_pil = ImageGrab.grab(bbox=(0, 40, 800, 640))
    print_screen_pil = ImageGrab.grab()
    org_screen = cv2.cvtColor(np.array(print_screen_pil), cv2.COLOR_BGR2RGB)
    return(org_screen)


def show_img(img):
    cv2.imshow('window', img)


def collect_live():

    once = 1
    img = ""
    while True:
        once = 0
        img = extract_image()
        img = compare(img)
        show_img(img)
        #gray_img = convert_to_gray(img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    # print(gray_img)


def compare(img):

    hero = cv2.imread('MY_HEROS/JUGG.png', cv2.IMREAD_UNCHANGED)
    #img = convert_to_gray(img)
    #hero = convert_to_gray(hero)
    #img = cv2.imread('MY_HEROS/Capture1.png', cv2.IMREAD_UNCHANGED)
    try:
        result = cv2.matchTemplate(img, hero, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_loc)
        print(max_val)

        threshold = 0.75
        if max_val >= threshold:
            print("found")
            hight = hero.shape[0]
            width = hero.shape[1]

            top_left = max_loc
            bottom_right = (top_left[0]+width, top_left[1]+hight)
            cv2.rectangle(img, top_left, bottom_right,
                          color=(0, 255, 0), lineType=cv2.LINE_4)
        else:
            print("not found")

    except:
        print("no img")

    return(img)


if __name__ == "__main__":
    print("start")
    collect_live()
    # compare()
