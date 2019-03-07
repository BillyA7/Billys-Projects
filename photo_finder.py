'''Program to search Pols laptop and get all the photos.'''

import os
import sys
import shutil
from itertools import chain

dst = sys.argv[1]

directorys = sys.argv[2:]

count = 0

# walks through all folders, subfolders and files using itertools.chain to search multiple directorys with os.walk
for root, subdirs, files in chain.from_iterable(os.walk(directory) for directory in directorys):
    for file in files:
        # needed to ignore useless photos
        if 'joey' not in os.path.join(root, file).lower() and 'e-bay' not in os.path.join(root, file).lower():
            # if the file extension is in the tuple, joins it with the root and copies it to the destination
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', '.bmp', '.png', '.pdd'):
                res = os.path.join(root, file)
                shutil.copy2(res, dst)
                print('Copying', file, 'to destination')
                count += 1

print('Done!')

if count == 0:
    print('No photos found.')

print(count, 'files copied.')
