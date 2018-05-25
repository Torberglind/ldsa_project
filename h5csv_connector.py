## imports
from os import walk, path
from utils import hdf5_getters
import csv
import time

import os
def recursive_file_search(rootDir, songs):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            recursive_file_search(path, songs)
        else:
            songs.append(str(path))


start = time.clock()
mypath="/home/ubuntu/data/"


songs = []
recursive_file_search(mypath, songs)

print("All songs in specified directory appended")

with open('songsABC.csv', 'w') as csvfile:
    fieldnames = ['track id', 'artist', 'title', 'loudness', 'tempo', 'tags', 'release year', 'danceability']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    num_songs = len(songs)
    perc_i = 0

    for song in songs:

        if songs.index(song)*10/num_songs > perc_i:
            print(str(perc_i*10)+"% done.")
            perc_i = perc_i + 1

        h5 = hdf5_getters.open_h5_file_read(song)

        track_id = str(hdf5_getters.get_song_id(h5), "utf-8")

        artist = str(hdf5_getters.get_artist_name(h5), "utf-8")

        title = str(hdf5_getters.get_title(h5), "utf-8")

        loudness = float(hdf5_getters.get_loudness(h5))

        release_year = int(hdf5_getters.get_year(h5))

        tempo = float(hdf5_getters.get_tempo(h5))
        
        danceability = float(hdf5_getters.get_danceability(h5))
        
        tags = hdf5_getters.get_artist_mbtags(h5)
        tags = tags.tolist()
        tags_refined = []
        for tag in tags:
            tags_refined.append(str(tag, "utf-8"))

        h5.close()

        writer.writerow({'track id': track_id,
                        'artist': artist,
                        'title': title,
                        'loudness': loudness,
                        'release year': release_year,
                        'tempo': tempo,
                        'tags': tags_refined
                        })

elapsed = (time.clock() - start)
print(Execution time:)
print(elapsed)