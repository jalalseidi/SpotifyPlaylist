from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Get user input
date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

# Set request headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Retrieve Billboard data
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract song names
song_names = [song.getText().strip() for song in soup.select("h3.c-title.a-no-trucate")]

# Print the top songs
if song_names:
    print(f"Top songs on {date}:")
    for idx, song in enumerate(song_names, start=1):
        print(f"{idx}. {song}")
else:
    print("Could not find song titles. The webpage structure may have changed.")

# Spotify Authentication
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
print(CLIENT_ID, CLIENT_SECRET)

scope = "playlist-modify-private"
song_uris = []
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        scope=scope,
        username="jay",
    ))
for song in song_names:
    result = sp.search(q=song, type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Could not find song: {song}")
print(song_uris)
user_id = sp.current_user()["id"]
# Step 1: Create a new private playlist
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist["id"]

print(f"Playlist '{playlist_name}' created successfully!")

# Step 2: Add songs to the playlist
if song_uris:
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
    print(f"Added {len(song_uris)} songs to the playlist!")
else:
    print("No valid songs found to add to the playlist.")

