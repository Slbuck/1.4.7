#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:26:03 2019

@author: Sydney
"""


import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            
import numpy as np


def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def frame_image(original_image, color, thickness):
    
    r, g, b = color
    imagewidth, imageheight = original_image.size
    
    frame = PIL.Image.new('RGBA', ((imagewidth + 2*thickness), (imageheight + 2*thickness)), (r, g, b, 255))
    frame.paste((original_image), (thickness, thickness))
    return frame

       
def frame_all_images(thickness, color, directory=None):
    
    if directory == None:
        directory = os.getcwd()
        
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        filename, filetype = file_list[n].split('.')
                
        framed_image = frame_image(image_list[n], color, thickness)
        
        framed_image_filename = os.path.join(new_directory, filename + '.png')
        framed_image.save(framed_image_filename)
    

