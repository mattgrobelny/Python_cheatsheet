import glob
from PIL import Image
import math
import re
import subprocess
import sys

# Dir for images
image_location = '/home/mgrobelny/Data/IB271/IB271_jpg/lab5/Dominate_colors_cluster_5/'
images_out ='Summary_images/'
png = '*.png'

# make directory for Summary_images
subprocess.call(["mkdir", image_location+images_out])


# Species file names
species_list = ['Corn','Amara', 'Radish','Oat','Pea', 'Tou','Twist']

# Condition list - regex expression to match from file names
Condition_list = ['high','low','new','old','high.*tip','high.*mid','high.*(base|bottom)','red|purple','green']


for species_file in species_list:
    # string for glob to produce list of files only .pngs
    glob_dir =image_location+species_file+'/'+png
    #print glob_dir
    condition_dictionary = {}
    for condition in Condition_list:
        condition_dictionary[condition] =[]

    # Get list of images to work on
    image_list = glob.glob(glob_dir)

    for image in image_list:

        #get image name
        image_name = image.split('/')[-1][0:-4]

        #print image_name
        # test image for condition group
        for condition in Condition_list:
            if re.search(condition, image_name,re.IGNORECASE):
                #add to condition group location of image if matching condition criteria
                condition_dictionary[condition].append(image)
            else:
                continue

    # for each dicitionary entry which contains files sorted for each condition
    # Import images and pile them on top of each other
    for condition in condition_dictionary.keys():
        # adapted from http://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
        print 'Working on:',species_file+'_'+condition

        # import group of images
        images = map(Image.open, condition_dictionary[condition])

        # get widths and heights of images if no images present then go to next condition
        try:
            widths, heights = zip(*(i.size for i in images))
        except ValueError:
            print "No images for condition"
            continue

        # Calc size of new image stack
        max_width = max(widths)
        sum_height = sum(heights)

        # define new image
        new_im = Image.new('RGB', (max_width, sum_height))

        # images spacer set to 0 for no space between stacked images
        y_offset = 0

        # Create image stack
        for im in images:
            new_im.paste(im, (0,y_offset))
            # incrament the paste point by image size
            y_offset += im.size[1]

        # Stack of dominate colors image output name and dir
        image_name_and_output_dir = image_location+images_out +'SUMMARY_'+species_file+'_'+condition+'_Dominate_colors.jpg'

        # Save new image 
        new_im.save(image_name_and_output_dir.replace('.*','_').replace('(base|bottom)','base'))
