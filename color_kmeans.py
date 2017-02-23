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
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# # ap.add_argument("-i", "--image", required=True, help="Path to the image")
# ap.add_argument("-c", "--clusters", required=True, type=int,
#                 help="# of clusters")
# args = vars(ap.parse_args())

# load the image and convert it from BGR to RGB so that
# image_list = ['Unknown',
#               'Unknown-2',
#               'Unknown-3',
#               'Unknown-4',
#               'Unknown-5',
#               'Unknown-6',
#               'Unknown-7',
#               'Unknown-8']
# image_list = ['1_Corn_Old_High_Tip_20x-page-001.jpg',
#               '1_Corn_Old_Low_Base_10x-page-001.jpg']
image_list = ['1_Corn_Old_High_Tip_20x.pdf',
              '1_Corn_Old_Low_Base_10x.pdf']
image_location = '/Users/matt/github/Python_cheats/Test_stain/'
cluster = 5
# Open image get color_distribution
for image in image_list:

    image_data = cv2.imread(image_location + image)
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
    hist_color = zip(hist, db.cluster_centers_)
    hist_out, color = zip(*hist_color)

    bar = utils.plot_colors(hist_out, color)

    # show our color bart
    plt.figure()
    plt.rcParams['savefig.facecolor'] = 'black'
    plt.suptitle(image, fontsize=20)
    plt.axis("off")
    plt.imshow(bar)
    plt.savefig(image_location + "Dominate_colors_%s.png" % (image), dpi=500)
    plt.close()
