# USAGE
# python color_kmeans.py --image images/jp.png --clusters 3
# from
# http://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/


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

# Dir for images
image_location = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/'
jpg = '*.jpg'

# string for glob to produce list of files only .jpgs
glob_dir =image_location+jpg
#print glob_dir

image_list = glob.glob(image_location+jpg)

# output location
image_location_output = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/Dominate_colors_cluster_9/'

# Number of dominate color groups to find for kmeans algorithm
cluster = 9

#counter
zero =1.0

for image in image_list:
    im = Image.open(image)
    image_name = image.split('/')[-1][0:-4]
    print "Working on:", image_name, "--- %s" %(zero/len(image_list)*100),'% done'
    zero +=1

    image_data = cv2.imread(image)
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
    bar = utils.plot_colors(hist_out, color)

    # show our color bart
    plt.figure()
    plt.rcParams['savefig.facecolor'] = 'grey'
    plt.suptitle(image_name, fontsize=20)
    plt.axis("off")
    plt.imshow(bar)
    plt.savefig(image_location_output + "%s_Dominate_colors.png" % (image_name), dpi=500)
    plt.close()
