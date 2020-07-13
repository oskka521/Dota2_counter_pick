import threading
import queue
import time
import cv2
import numpy as np
from PIL import Image, ImageGrab


def extract_image(opt=1):
    # print_screen_pil = ImageGrab.grab(bbox=(0, 40, 800, 640))

    if opt == 1:
        print_screen_pil = ImageGrab.grab()
        org_screen = cv2.cvtColor(np.array(print_screen_pil), cv2.COLOR_BGR2GRAY)
    else:
        print_screen_pil = Image.open("DATA/Capture11.png")
        org_screen = cv2.cvtColor(np.array(print_screen_pil), cv2.COLOR_RGB2GRAY)

    return org_screen


def read_hero_names():
    f = open("DATA/names2.txt")
    names_list = f.readlines()
    new_names = []
    for i in range(len(names_list)):
        new_names.append(str(names_list[i][: str(names_list[i]).find(".")]))
    f.close()
    print(new_names)
    return new_names


def find_heroes_in_image(img):
    store_list = []
    heros_name = read_hero_names()

    for hero in heros_name:

        template = cv2.cvtColor(
            np.array(Image.open("DATA/HEROS/" + hero + ".png")), cv2.COLOR_RGB2GRAY
        )

        try:
            result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            threshold = 0.80
            if max_val >= threshold:
                store_list.append([hero, max_val, max_loc])
            else:
                pass
                # print("not found", hero)
        except:
            print("no match")
    return store_list


def place_in_radiant_or_dire(store_list):
    for i in range(len(store_list)):
        if store_list[i][2][0] < 800:
            store_list[i].append("radiant")
        else:
            store_list[i].append("dire")


def collect_img(opt):
    screen_img = extract_image(opt)
    store_list = find_heroes_in_image(screen_img)

    place_in_radiant_or_dire(store_list)
    # for i in range(len(store_list)):
    #    print(store_list[i])
    return store_list


def run(q1, OPTIONS):
    print("image_process_function working")
    store_list = collect_img(OPTIONS)
    return store_list

