import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import io

image0 = np.load("images/car_0.npy")
image1 = np.load("images/car_1.npy")
image2 = np.load("images/car_2.npy")
image3 = np.load("images/car_3.npy")
image4 = np.load("images/car_4.npy")
image5 = np.load("images/car_5.npy")
image6 = np.load("images/car_6.npy")
image7 = np.load("images/car_7.npy")
image8 = np.load("images/car_8.npy")

images = [image0, image1, image2, image3, image4, image5, image6, image7, image8]

"""
returns sum of pixels from all images
"""
def sum_total():
    sum = 0
    for i in range(len(images)):
        sum += np.sum(images[i])
    return sum

"""
returns an array including sum of pixels for each image
"""
def sum_per_image():
    sum = []
    for i in range(len(images)):
        sum.append(np.sum(images[i]))
    return sum
"""
returns image's index with maximum number of pixels
"""
def sum_max():
    sum_per_images = sum_per_image()
    return sum_per_images.index(max(sum_per_images))

def mean_image():
    mean_image_value = np.zeros((400,600))
    for i in range(len(images)):
        mean_image_value += images[i]
    mean_image_value /= len(images)
    return mean_image_value

def standard_deviation():
    return np.std(images)

def normalize():
    normalized_image = np.zeros((400, 600))
    for i in range(len(images)):
        normalized_image = (images[i] - mean_image()) / standard_deviation()
        io.imshow(normalized_image.astype(np.uint8))
        io.show()

def crop_image():
    cropped_image = np.zeros((100, 120))
    for i in range(len(images)):
        cropped_image = images[i][200:300, 280:400]
        io.imshow(cropped_image.astype(np.uint8))
        io.show()


if __name__ == '__main__':
    sum_total_value = sum_total()
    print(sum_total_value)
    sum_per_images = sum_per_image()
    print(sum_per_images)
    sum_max_value = sum_max()
    print(sum_max_value)
    standard_deviation_value = standard_deviation()
    print(standard_deviation_value)
    crop_image()
    io.imshow(mean_image().astype(np.uint8))
    io.show()
