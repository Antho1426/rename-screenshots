#!/usr/local/bin/python3.6


# rename_screenshots.py


## Required packages
import os
import glob
import pickle as cPickle

## Procedure

# 1) Getting all the ".jpg", ".png", ".gif" and ".mov" files situated on the Desktop
list_JPG_Desktop = glob.glob("/Users/anthony/Desktop/*.jpg")
list_PNG_Desktop = glob.glob("/Users/anthony/Desktop/*.png")
list_GIF_Desktop = glob.glob("/Users/anthony/Desktop/*.gif")
list_MOV_Desktop = glob.glob("/Users/anthony/Desktop/*.mov")
list_Desktop = list_JPG_Desktop + list_PNG_Desktop + list_GIF_Desktop + list_MOV_Desktop

# 2) Getting all the ".jpg", ".png" and ".mov" files situated on the Desktop and
# containing the string "Screenshot"
list_Screenshots_Desktop = []
for i in range(len(list_Desktop)):
    if "Screenshot " in list_Desktop[i]:
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
    new_path = path.replace('Screenshot ', '')
    # ===================================================

    os.rename(path, new_path)


if len(list_Screenshots_Desktop) > 0:
    # Posting macOS X notification
    from pync import Notifier
    Notifier.notify('Screenshots renamed!')