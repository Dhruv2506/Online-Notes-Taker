# Name : Dhruv Patel

# python script to takes notes during online class

# imgcompare library is used to get the percentage difference between two images

import imgcompare
import numpy as np
import cv2
import pyautogui
import os
import time
from datetime import date


# get_screenshot function is used to get the screenshot
def get_screenshot(name):
    image = pyautogui.screenshot()  # take the screenshot
    image = cv2.cvtColor(np.array(image),  # change the image to RGB form
                         cv2.COLOR_RGB2BGR)
    cv2.imwrite(name, image)  # save image in folder


# get_diff function to get the diff between two images
def get_diff(a, b):
    return imgcompare.image_diff_percent(a, b)  # returns the difference in image


def make_directory():  # makes the directory using current date
    try:
        os.mkdir('/' + "lecture_notes_" + str(date.today()))
    except:
        print("directory already exists")


# take_screenshots function to take screenshots during lecture

def take_screenshots(total_time, incr):
    f = '/' + "lecture_notes_" + str(date.today())
    curr_time = 0
    count = 1

    time.sleep(10)

    while curr_time < total_time:
        get_screenshot(f + "//" + str(count) + ".png")
        count += 1
        time.sleep(incr)
        curr_time += incr


# remove image function to remove the similar images

# This function start traversing from the last and keep on removing the similar images

def remove_same_images():
    directory = '/' + "ENV_lecture_notes_" + str(date.today())
    a = os.listdir('/' + "ENV_lecture_notes_" + str(date.today()))
    delete_list = []

    last = len(a)

    for x in range(len(a) - 1, 1, -1):
        y = get_diff(directory + "//" + str(x) + ".png", directory + "//" + str(last) + ".png")

        if y < 1:
            delete_list.append(directory + "//" + str(x) + ".png")
        else:
            last = x

    for x in delete_list:
        os.remove(x)


# main function

if __name__ == '__main__':
    make_directory()
    print("Enter the total time of your lecture in minutes : ")
    n = int(input())
    print("Running......")
    print("-> Please try to avoid switching tabs")
    print("-> If your lecture end before the time you described , run the remove_similar_image.py ")
    take_screenshots(n * 60, 5)
