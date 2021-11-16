import face_recognition
from PIL import Image, ImageTk
import os
import cv2 as cv
import time

from numpy import inexact

BASE_DIR = os.getcwd()
dir_path = os.path.join(BASE_DIR, 'test_image')

def crop_image(dir_image):
    image = face_recognition.load_image_file(dir_image)
    face_locations = face_recognition.face_locations(image)
    # print(face_locations)

    # print("Tìm được {} khuôn mặt trong bức ảnh.".format(len(face_locations)))
    index = 0
    lst_image_detection = []
    for face_location in face_locations:
        # in tung anh và vi tri
        top, right, bottom, left = face_location
        # print("Khuôn mặt nằm ở vị trí pixel Top: {}, Right: {}, Bottom: {}, Left: {}".format(
        #     top, right, bottom, left))

        # luu anh
        name_image = ''
        location_1 = 0
        try:
            location_1 = dir_image.rindex("\\")+1
            name_image = dir_image[location_1:]
            location_2 = name_image.rindex('.')
            name_image = name_image[:location_2]
        except:
            location_1 = dir_image.rindex("/")+1
            name_image = dir_image[location_1:]
            location_2 = name_image.rindex('.')
            name_image = name_image[:location_2]
        face_image = image[top:bottom, left:right]
        name_image_detection = '{}{}{}.png'.format('D:/Baitapcacmon/Laptrinhhethong/face/image_detection/',name_image+'_pic', index)
        dict_info = {}
        dict_info['file_path'] = name_image_detection
        dict_info['note'] = 'Ảnh khuôn mặt thứ ' + str(index+1) + ' cắt từ ' + dir_image[location_1:]
        lst_image_detection.append(dict_info)
        Image.fromarray(face_image).save('{}{}{}.png'.format('D:/Baitapcacmon/Laptrinhhethong/face/image_detection/',name_image+'_pic', index))
        index+=1

        # truy cập ảnh
        # face_image = image[top:bottom, left:right]
        # pil_image = Image.fromarray(face_image)
        # pil_image.show()

    return lst_image_detection


def read_file_from_folder(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        img_path = os.path.join(dir_path, file)
        image = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        cv.imshow('image', image)
        cv.waitKey(3000)
    cv.destroyAllWindows()
    return True


def get_list_file_path_from_folder(dir_path):
    files = os.listdir(dir_path)
    list_file_path = []
    for file in files:
        img_path = os.path.join(dir_path, file)
        list_file_path.append(img_path)
    return list_file_path

# read_file_from_folder(dir_path)
# list_file_path = get_list_file_path_from_folder(dir_path)
# for file_path in list_file_path:
#     crop_image(file_path)
