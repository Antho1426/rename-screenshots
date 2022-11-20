#!/usr/local/bin/python3.6


# rename_screenshots.py


## Required packages
import os
import glob
import pickle as cPickle

## Procedure
#-------------------------------

#++++++++++++++++++++++++++++++
beginning_word_to_replace = "Screenshot "
#++++++++++++++++++++++++++++++

# 1) Getting all the ".jpg", ".png", ".gif" and ".mov" files situated on the Desktop
list_JPG_Desktop = glob.glob("/Users/anthony/Desktop/*.jpg")
list_PNG_Desktop = glob.glob("/Users/anthony/Desktop/*.png")
list_GIF_Desktop = glob.glob("/Users/anthony/Desktop/*.gif")
list_MOV_Desktop = glob.glob("/Users/anthony/Desktop/*.mov")
list_Desktop = list_JPG_Desktop + list_PNG_Desktop + list_GIF_Desktop + list_MOV_Desktop

# 2) Getting all the ".png" and ".mov" files situated on the Desktop and
# containing the string stored in the variable "beginning_word_to_replace"
list_Screenshots_Desktop = []
for i in range(len(list_Desktop)):
    if beginning_word_to_replace in list_Desktop[i]:
        list_Screenshots_Desktop.append(list_Desktop[i])

# 3) Renaming all the target files situated on the Desktop and containing the
# string "Screenshot"
for i in range(len(list_Screenshots_Desktop)):
    path = list_Screenshots_Desktop[i]

    #===================================================
    # Replacing the word "Screenshot " (i.e. the word "Screenshot" followed by a
    # space " ") by an EMPTY space (we could choose to replace the word
    # "Screenshot" by something else or to modify the name of the screenshots
    # differently, but I just want the word "Screenshot " to disappear and to
    # keep the date)
    new_path = path.replace(beginning_word_to_replace, '')
    # Below adjustments are intended to match "Snagit" screenshot format: yyyy-mm-dd_hh-mm-ss
    # (This way, a screenshot initially named "Screenshot yyyy-mm-dd at hh.mm.ss" will finally be converted into "yyyy-mm-dd_hh-mm-ss")
    #------
    new_path = new_path.replace(' at ', '_')
    split = new_path.split('.')
    comb = '-'.join(split[:3])
    new_path = '.'.join([comb, split[-1]])
    #------
    #===================================================

    os.rename(path, new_path)

#-------------------------------

if len(list_Screenshots_Desktop) > 0:
    print("Screenshot(s) successfully renamed!") # If we have a "Large Type" block connected at the output of the "/bin/bash Run Script" block, this will print "Screenshots renamed!" on the screen
else:
    print("No screenshot to rename...")
