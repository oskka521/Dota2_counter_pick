from PIL import Image, ImageGrab
import cv2
import numpy as np


def show_img(img):
    cv2.imshow('window', img)


def collect_live(img):

    once = 1
    while True:
        once = 0
        show_img(img)
        # gray_img = convert_to_gray(img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# img = cv2.cvtColor(numpy.array(ImageGrab.grab()), cv2.COLOR_RGB2BGR)
# img = numpy.array(Image.open('MY_HEROS/Capture3.png'), cv2.COLOR_RGB2BGR)
img = np.array(cv2.imread('MY_HEROS/Capture1.png', cv2.COLOR_RGB2BGR))

template = cv2.cvtColor(np.array(
    Image.open('MY_HEROS/jugg.png')), cv2.COLOR_RGB2BGR)

found_img = True

try:
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(max_loc)
    print(max_val)

    threshold = 0.80

    if max_val >= threshold:
        print("found")
        hight = template.shape[0]
        width = template.shape[1]

        top_left = max_loc
        bottom_right = (top_left[0]+width, top_left[1]+hight)
        cv2.rectangle(img, top_left, bottom_right,
                      color=(0, 255, 0), lineType=cv2.LINE_4)
        collect_live(img)

        show_img(img)
        collect_live(img)
    else:
        print(template.shape)
except:
    print("error")
