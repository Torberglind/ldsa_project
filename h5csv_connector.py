
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
    fieldnames = ['track id', 'artist', 'title', 'danceability', 'loudness', 'tempo', 'energy', 'tags', 'release year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for song in songs:
        h5 = hdf5_getters.open_h5_file_read(song)

        track_id = str(hdf5_getters.get_song_id(h5), "utf-8")

        artist = str(hdf5_getters.get_artist_name(h5), "utf-8")

        title = str(hdf5_getters.get_title(h5), "utf-8")

        danceability = hdf5_getters.get_danceability(h5)

        loudness = hdf5_getters.get_loudness(h5)

        release_year = hdf5_getters.get_year(h5)

        tempo = hdf5_getters.get_tempo(h5)

        tags = hdf5_getters.get_artist_mbtags(h5)
        tags = tags.tolist()
        tags_refined = []
        for tag in tags:
            tags_refined.append(str(tag, "utf-8"))

        energy = hdf5_getters.get_energy(h5)

        h5.close()

        writer.writerow({'track id': track_id,
                        'artist': artist,
                        'title': title,
                        'danceability': danceability,
                        'loudness': loudness,
                        'release year': release_year,
                        'tempo': tempo,
                        'energy': energy,
                        'tags': tags_refined
                        })

