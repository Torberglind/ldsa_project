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

mypath=""


songs = []
recursive_file_search(mypath, songs)

print("All songs in specified directory appended")

with open('songs.csv', 'w') as csvfile:
    fieldnames = ['artist_mbid', 'artist_mbtags', 'artist_name', 'artist_playmeid', 'artist_terms', 'artist_terms_freq',
                  'artist_terms_weight', 'audio_md5', 'bars_confidence', 'bars_start', 'beats_confidence', 'beats_start',
                  'danceability', 'duration', 'end_of_fade_in', 'energy', 'key', 'key_confidence', 'loudness',
                  'mode', 'mode_confidence', 'release', 'sections_confidence', 'sections_start', 'segments_confidence',
                  'segments_loudness_max', 'segments_loudness_max_time', 'segments_loudness_start', 'segments_pitches',
                  'segments_start', 'segments_timbre', 'similar_artists', 'song_hotttnesss', 'song_id', 'start_of_fade_out',
                  'tatums_confidence', 'tatums_start', 'tempo', 'time_signature', 'time_signature_confidence', 'title',
                  'track_7digitalid', 'track_id', 'year']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


    for song in songs:
        h5 = hdf5_getters.open_h5_file_read(song)
        artist_mbid = hdf5_getters.get_artist_mbid(h5)
        artist_mbtags = hdf5_getters.get_artist_mbtags(h5)
        artist_name = hdf5_getters.get_artist_name(h5)
        artist_playmeid = hdf5_getters.get_artist_playmeid(h5)
        artist_terms = hdf5_getters.get_artist_7digitalid(h5)
        artist_terms_freq = hdf5_getters.get_artist_terms_freq(h5)
        artist_terms_weight = hdf5_getters.get_artist_terms_weight(h5)
        audio_md5 = hdf5_getters.get_audio_md5(h5)
        bars_confidence = hdf5_getters.get_bars_confidence(h5)
        bars_start = hdf5_getters.get_bars_start(h5)
        beats_confidence = hdf5_getters.get_beats_confidence(h5)
        beats_start = hdf5_getters.get_beats_start(h5)
        danceability =  hdf5_getters.get_danceability(h5)
        duration = hdf5_getters.get_duration(h5)
        end_of_fade_in = hdf5_getters.get_end_of_fade_in(h5)
        energy = hdf5_getters.get_energy(h5)
        key = hdf5_getters.get_key(h5)
        key_confidence = hdf5_getters.get_key_confidence(h5)
        loudness = hdf5_getters.get_loudness(h5)
        mode = hdf5_getters.get_mode(h5)
        mode_confidence = hdf5_getters.get_mode_confidence(h5)
        release = hdf5_getters.get_release(h5)
        sections_confidence = hdf5_getters.get_sections_confidence(h5)
        sections_start = hdf5_getters.get_sections_start(h5)
        segments_confidence = hdf5_getters.get_segments_confidence(h5)
        segments_loudness_max = hdf5_getters.get_segments_loudness_max(h5)
        segments_loudness_max_time = hdf5_getters.get_segments_loudness_max_time(h5)
        segments_loudness_start = hdf5_getters.get_segments_loudness_start(h5)
        segments_pitches = hdf5_getters.get_segments_pitches(h5)
        segments_start = hdf5_getters.get_segments_start(h5)
        segments_timbre = hdf5_getters.get_segments_timbre(h5)
        similar_artists = hdf5_getters.get_similar_artists(h5)
        song_hotttnesss = hdf5_getters.get_song_hotttnesss(h5)
        song_id = hdf5_getters.get_song_id(h5)
        start_of_fade_out = hdf5_getters.get_start_of_fade_out(h5)
        tatums_confidence = hdf5_getters.get_tatums_confidence(h5)
        tatums_start = hdf5_getters.get_tatums_start(h5)
        tempo = hdf5_getters.get_tempo(h5)
        time_signature = hdf5_getters.get_time_signature(h5)
        time_signature_confidence = hdf5_getters.get_time_signature_confidence(h5)
        title = hdf5_getters.get_title(h5)
        track_7digitalid = hdf5_getters.get_track_7digitalid(h5)
        track_id = hdf5_getters.get_track_id(h5)
        year = hdf5_getters.get_year(h5)

        h5.close()
        writer.writerow({
            'artist_mbid': artist_mbid,
            'artist_mbtags': artist_mbtags,
            'artist_name': artist_name,
            'artist_playmeid': artist_playmeid,
            'artist_terms': artist_terms,
            'artist_terms_freq': artist_terms_freq,
            'artist_terms_weight': artist_terms_weight,
            'audio_md5': audio_md5,
            'bars_confidence': bars_confidence,
            'bars_start': bars_start,
            'beats_confidence': beats_confidence,
            'beats_start': beats_start,
            'danceability': danceability,
            'duration': duration,
            'end_of_fade_in': end_of_fade_in,
            'energy': energy,
            'key': key,
            'key_confidence': key_confidence,
            'loudness': loudness,
            'mode': mode,
            'mode_confidence': mode_confidence,
            'release': release,
            'sections_confidence': sections_confidence,
            'sections_start': sections_start,
            'segments_confidence': segments_confidence,
            'segments_loudness_max': segments_loudness_max,
            'segments_loudness_max_time': segments_loudness_max_time,
            'segments_loudness_start': segments_loudness_start,
            'segments_pitches': segments_pitches,
            'segments_start': segments_start,
            'segments_timbre': segments_timbre,
            'similar_artists': similar_artists,
            'song_hotttnesss': song_hotttnesss,
            'song_id': song_id,
            'start_of_fade_out': start_of_fade_out,
            'tatums_confidence': tatums_confidence,
            'tatums_start': tatums_start,
            'tempo': tempo,
            'time_signature': time_signature,
            'time_signature_confidence': time_signature_confidence,
            'title': title,
            'track_7digitalid': track_7digitalid,
            'track_id': track_id,
            'year': year})