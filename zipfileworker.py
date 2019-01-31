import logging
from logging import NullHandler
import zipfile
import os, os.path
from os import walk
import time

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())

def task_getfilenames(rootdir):
    filenames = []
    for dir in rootdir:
        if len(dir[-1]) > 0:
            for zipfilename in dir[-1]:
                file = zipfile.ZipFile(os.path.join(dir[0], zipfilename))
                filenames.append(file.namelist())
    return filenames

def task_writeouput(list_filenames):
    with open('./BuildOutput/results_output_{date}.txt'.format(date=time.strftime("%Y%m%d-%H")), 'w') as output:
        for filetree in list_filenames:
            for file in filetree[1:]:
                output.write('{buildname}|{filepath}\n'.format(buildname=filetree[0], filepath= file))

def dojob(zippath):

    #Task 1 get the root directory
    rootdir = walk('./BuildArtifacts/')
    if not os.path.exists("./BuildOutput/"):
        os.makedirs("./BuildOutput/")
    
    # Task 2 get filenames from Zip
    list_filenames = task_getfilenames(rootdir)

    # Task 3 : write the output data
    task_writeouput(list_filenames)