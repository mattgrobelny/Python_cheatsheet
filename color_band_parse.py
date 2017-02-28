import os
import sys
import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm
import glob

#
# Goal of Script: 1) Pull of a histogram of pixel and their color values
#                 2) Output a lineplot of color value distribution for each color band (R, G, B)
#

# Dir for images
image_location = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/'
jpg = '*.jpg'

# string for glob to produce list of files only .jpgs
glob_dir =image_location+jpg

#print glob_dir

# Save list of jpg files to var
image_list = glob.glob(image_location+jpg)

# output location
image_location_output = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/Spectrum_out/'

x_val = range(256)
image_hist_dic = {}
patches_list = []
# Open image get color_distribution
for image in image_list:
    # open image
    im = Image.open(image)

    # Pull out image name from file name
    image_name = image.split('/')[-1][0:-4]
    print "Working on:", image_name

    # image specs
    width, height = im.size

    #get histogram distribtion of pixel colors
    color_distribution = im.histogram()
    total_pixels = float(width * height)

    # prep vars
    color_distribution_percent = []
    red = []
    blue = []
    green = []

    # split histogram by color
    for i in range(256):
        red.append(float(color_distribution[i]))
        blue.append(float(color_distribution[257 + i]))
        green.append(float(color_distribution[512 + i]))
    image_hist_dic[image_name] = [red, blue, green]

# Plot color distribtion for each band
for key in image_hist_dic.keys():
    print "Image output Working on:", key
    # Plot R
    plt.plot(x_val, image_hist_dic[key][0], color='red')
    # Plot B
    plt.plot(x_val, image_hist_dic[key][1], color='blue')
    # Plot G
    plt.plot(x_val, image_hist_dic[key][2], color='green')
    plt.xlim(0, 256)
    plt.suptitle(key, fontsize=20)
    plt.ylabel('Pixel counts')
    plt.xlabel('Color Intensity')

    # Save figure
    plt.savefig(image_location_output + "%s_Specturm.png" % (key), dpi=500)
    plt.close()
