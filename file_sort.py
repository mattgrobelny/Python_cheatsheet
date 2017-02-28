import subprocess
import glob
import re

#
# Goal of Script: 1) Sort dominate colors by species
#

# Dir for images
image_location = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/Dominate_colors_cluster_5/'
png = '.png'

# string for glob to produce list of files only .jpgs
glob_dir =image_location+'*'+png
#print glob_dir

image_list = glob.glob(glob_dir)

species_list = ['Corn','Amara', 'Radish','Oat','Pea', 'Tou','Twist']
for species in species_list:
    # make files for each species
    subprocess.call(["mkdir", image_location+species])

for image in image_list:
  image_name = image.split('/')[-1][0:-4]
  print "Working on:", image_name
  for species in species_list:
     # if species name matches file crop file and save to species specific file
    if re.search(species, image_name):
        subprocess.call(["convert", image,'-crop','3075x290+500+1250',image_location+species+'/'+image_name+png])
