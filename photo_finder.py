'''Program to search Pols laptop and get all the photos.'''

import os
import shutil
import time
from itertools import chain

print('This script will search your specified directorys for photos and copy them to your specified destination.')

time.sleep(2)

directorys = input('Please enter all the directorys you would like to search\n--->')

time.sleep(1)

dst = input('Please enter the destination folder path\n--->')

time.sleep(1)
print('Scanning directorys...\n')
time.sleep(1)

count = 0

# use first for loop for single directory
# for root, subdirs, files in os.walk(directorys):
# walks through all folders, subfolders and files using itertools.chain to search multiple directorys with os.walk
for root, subdirs, files in chain.from_iterable(os.walk(directory) for directory in directorys):
    for file in files:
        # ignore useless photos
        if 'joey' not in os.path.join(root, file).lower() and 'e-bay' not in os.path.join(root, file).lower():
            # if the file extension is in the tuple, joins it with the root and copies it to the destination
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', '.bmp', '.png', '.gif', '.pdd'):
                res = os.path.join(root, file)
                shutil.copy2(res, dst)
                print('Copying', file, 'to', dst)
                count += 1
                if count % 50 == 0:
                    time.sleep(1)
                    print('\nScanning directorys...\n')
                    time.sleep(1)

print('\nFinished!')

time.sleep(1)

if count == 0:
    print('\nNo photos found.')

print('\n', count, 'files copied to', dst)
