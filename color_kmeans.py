# adapted from
# http://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/

#
# Goal of Script: 1) Find X number of dominate colors from lab5 scope images
#                 2) Sort by color intensities
#                 2) Plot dominate colors

# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# import argparse
import utils
import cv2
from sklearn import metrics
import numpy as np
import glob
from PIL import Image
import math

# Dir for images
image_location = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/'
jpg = '*.jpg'

# string for glob to produce list of files only .jpgs
glob_dir =image_location+jpg
#print glob_dir

# Get list of images to work on
image_list = glob.glob(image_location+jpg)

# output location
image_location_output = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/Dominate_colors_cluster_9/'

# Number of dominate color groups to find for kmeans algorithm
cluster = 9

#counter
zero =1.0

for image in reversed(image_list):
    im = Image.open(image)
    image_name = image.split('/')[-1][0:-4]
    print "Working on:", image_name, "--- %s" % (int(zero/len(image_list)*100)),'% done'
    zero +=1

    image_data = cv2.imread(image)
    # image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
    image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)


    # reshape the image to be a list of pixels
    image_data = image_data.reshape(
        (image_data.shape[0] * image_data.shape[1], 3))

    # cluster the pixel intensities
    db = KMeans(n_clusters=cluster)
    db.fit(image_data)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(db)
    #bar = utils.plot_colors(hist, db.cluster_centers_)

    # reorganize colors
    hist_color = zip(hist, db.cluster_centers_)
    hist_out, color = zip(*hist_color)


    # print hist_out, color
    # set up dictionary and list to sort colors
    intensity_dict ={}
    color_sorted_by_int =[]

    # convert RGB to intensity
    for hist, col in hist_color:
        # get intensity values
        intensity = (0.299*col[0] + 0.587*col[1] + 0.114*col[2])
        # Color intensity convert EQ from https://www.w3.org/TR/AERT#color-contrast
        intensity_dict[intensity] = [hist,col]

    # sort colors
    for key in sorted(intensity_dict.keys()):
        color_sorted_by_int.append(intensity_dict[key])

    hist_out, color = zip(*color_sorted_by_int)

    bar = utils.plot_colors(hist_out, color)

    # show our color bar
    plt.figure()
    plt.rcParams['savefig.facecolor'] = 'grey'
    plt.suptitle(image_name, fontsize=20)
    plt.axis("off")
    plt.imshow(bar)
    plt.savefig(image_location_output + "%s_Dominate_colors.png" % (image_name), dpi=500)
    plt.close()
