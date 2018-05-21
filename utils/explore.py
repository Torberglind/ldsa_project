## imports
from os import walk, path
import hdf5_getters

import os
def recursive_file_search(rootDir, songs):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)

        if os.path.isdir(path):
            recursive_file_search(path, songs)
        else:
            songs.append(str(path))


mypath="MillionSongSubset/data/A/B"

songs = []
recursive_file_search(mypath, songs)

print("All songs in specified directory appended")

for song in songs:
    h5 = hdf5_getters.open_h5_file_read(song)
    timbre = hdf5_getters.get_segments_timbre(h5)
    print(timbre.shape)
    h5.close()
