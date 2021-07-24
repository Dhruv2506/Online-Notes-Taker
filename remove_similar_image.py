# Name : Dhruv Patel
# This program removes the similar images if lecture ends before the time given by you

import os
import imgcompare


def get_diff(a, b):
    return imgcompare.image_diff_percent(a, b)


def remove_same_images():
    directory = r"C:\Users\patel\OneDrive\Desktop\ENV_lecture_notes_2021-01-27"
    a = os.listdir(directory)
    delete_list = []

    last = len(a)

    for x in range(len(a) - 1, 1, -1):
        y = get_diff(directory + "//" + str(x) + ".png", directory + "//" + str(last) + ".png")

        if y < 5:
            delete_list.append(directory + "//" + str(x) + ".png")
        else:
            last = x

    for x in delete_list:
        os.remove(x)


if __name__ == '__main__':
    remove_same_images()
