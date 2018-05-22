
## imports
from os import walk, path
from utils import hdf5_getters
import csv

import os
def recursive_file_search(rootDir, songs):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)

        if os.path.isdir(path):
            recursive_file_search(path, songs)
        else:
            songs.append(str(path))


mypath="/Users/torberglind/Data-sets/MillionSongSubset/data/a/A/B/"

songs = []
recursive_file_search(mypath, songs)

print("All songs in specified directory appended")

with open('songs2.csv', 'w') as csvfile:
    fieldnames = ['track id', 'artist', 'title', 'danceability', 'loudness', 'release year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for song in songs:
        h5 = hdf5_getters.open_h5_file_read(song)
        trackId = str(hdf5_getters.get_song_id(h5), "utf-8")
        artist = str(hdf5_getters.get_artist_name(h5), "utf-8")
        title = str(hdf5_getters.get_title(h5), "utf-8")
        danceability = str(hdf5_getters.get_danceability(h5), "utf-8")
        loudness = str(hdf5_getters.get_loudness(h5), "utf-8")
        releaseYear = str(hdf5_getters.get_release(h5), "utf-8")
        h5.close()
        writer.writerow({'track id': trackId,
                         'artist': artist,
                         'title': title,
                         'danceability': danceability,
                         'loudness': loudness,
                         'release year': releaseYear})