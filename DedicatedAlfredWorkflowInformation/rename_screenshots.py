#!/usr/local/bin/python3.6


# rename_screenshots.py
# Python script that automatically renames the Screenshots situated on the Desktop



## Required packages
import os
import sys
import glob
import pickle as cPickle
from workflow import Workflow





def main(wf):



    ## Procedure
    #-------------------------------

    # 1) Getting all the ".png" and ".mov" files situated on the Desktop
    list_PNG_Desktop = glob.glob("/Users/anthony/Desktop/*.png")
    list_MOV_Desktop = glob.glob("/Users/anthony/Desktop/*.mov")
    list_PNG_MOV_Desktop = list_PNG_Desktop + list_MOV_Desktop

    # 2) Getting all the ".png" and ".mov" files situated on the Desktop and
    # containing the string "Screenshot"
    list_Screenshots_Desktop = []
    for i in range(len(list_PNG_MOV_Desktop)):
        if "Screenshot " in list_PNG_MOV_Desktop[i]:
            list_Screenshots_Desktop.append(list_PNG_MOV_Desktop[i])

    # 3) Renaming all the ".png" files situated on the Desktop and containing the
    # # string "Screenshot"
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

    #-------------------------------


    if len(list_Screenshots_Desktop) > 0:
        print("Screenshot(s) successfully renamed!") # If we have a "Large Type" block connected at the output of the "/bin/bash Run Script" block, this will print "Screenshots renamed!" on the screen
    else:
        print("No screenshot to rename...")






if __name__ == u'__main__':
    wf = Workflow()
    sys.exit(wf.run(main))

