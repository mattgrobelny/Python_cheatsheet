import os
import sys
import numpy as np
import math
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm


# import getopt
#
# # define variables and defaults
# kmer = 0
# file_name = ""
#
# # pass in commmands line args array
# argv = sys.argv[1:]
#
# # Get options demo for a script which takes in a file and a kmer parameter
#
# try:
#     # h does not require input so the is no : after it
#     opts, args = getopt.getopt(argv, "hk:f:")
# except getopt.GetoptError:
#     print 'kmer.py -k <kmer_size> -f <inputfile>'
#     sys.exit(2)
# for opt, arg in opts:
#     if opt == '-h':
#         print 'kmer.py -k <kmer_size> -f <inputfile>'
#         sys.exit()
#     elif opt in ("-k"):
#         kmer = arg
#     elif opt in ("-f"):
#         file_name = arg
# print "Kmer size is:", kmer
# print "Input file is:", file_name

image_list = ['Unknown',
              'Unknown-2',
              'Unknown-3',
              'Unknown-4',
              'Unknown-5',
              'Unknown-6',
              'Unknown-7',
              'Unknown-8',
              'Unknown-9']
image_location = '/Users/matt/github/Python_cheats/Fruit_imgs/'
x_val = range(256)
image_hist_dic = {}

# Open image get color_distribution
for image in image_list:
    im = Image.open(image_location + image)
    width, height = im.size
    color_distribution = im.histogram()
    total_pixels = float(width * height)
    color_distribution_percent = []
    for i in range(len(color_distribution)):
        color_distribution_percent.append(
            (float(color_distribution[i]) / float(total_pixels)) * 100)

        image_hist_dic[image] = color_distribution_percent
for key in image_hist_dic.keys():

    # Plot R
    plt.plot(x_val, image_hist_dic[key][0:256], color='red')
    # Plot B
    plt.plot(x_val, image_hist_dic[key][257:513], color='blue')
    # Plot G
    plt.plot(x_val, image_hist_dic[key][512:769], color='green')
    plt.xlim(150, 256)
    # plt.axvline(x=image_hist_dic[key][0:256].index(
    #     max(image_hist_dic[key][0:256])), color='red')
    # plt.axvline(x=image_hist_dic[key][257:513].index(
    #     max(image_hist_dic[key][257:513])), color='blue')
    # plt.axvline(x=image_hist_dic[key][512:769].index(
    #     max(image_hist_dic[key][512:769])), color='green')

    # print "Max R", color_distribution[0:256].index(
    #     max(color_distribution[0:256]))
    # print "Max B", color_distribution[257:513].index(
    #     max(color_distribution[257:513]))
    # print "Max G", color_distribution[512:769].index(
    #     max(color_distribution[512:769]))

    plt.show()

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(X)

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))
