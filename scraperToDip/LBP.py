
import skimage.io
from skimage import data_dir

from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import label2rgb
import cv2

# settings for LBP
radius = 3
n_points = 8 * radius

image = skimage.data.load('D:\\Github\\FYP\\images\\ctdp18412\\local33.jpg','as_grey')
# convert this image to 2D

# image = data.load(coll)
lbp = local_binary_pattern(image, n_points, radius)
