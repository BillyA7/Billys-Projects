'''Program to delete converted pdd files from specified folder.'''

import os
import sys

directory = sys.argv[1]

count = 0

for filename in os.listdir(directory):
    # finds all files with pdd extension and permanently deletes them
    if filename.lower().endswith('.pdd'):
        os.unlink(os.path.join(directory, filename))
        print('Deleting', filename)
        count += 1

print('Done!')

if count == 0:
    print('No pdd files found.')

print(count, 'files deleted.')
