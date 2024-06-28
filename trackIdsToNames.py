from yandex_music import Client
import json

track_list_file_path=input("Enter path to file which contains trackIds: ")
tracks_list_ids = []
with open(track_list_file_path, "r") as file:
    tracks_list_ids = json.load(file)["trackIds"]

tracks_list_ids = list(dict.fromkeys(tracks_list_ids))
client = Client().init()
tracks = client.tracks(tracks_list_ids)
for track in tracks:
    with open('tracks.txt', 'a') as file:
        file.write(f"{track.title} - {track.artists_name()[0]}\n")
