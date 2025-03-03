# Billboard Hot 100 to Spotify Playlist

This project scrapes the Billboard Hot 100 chart for a user-specified date and creates a Spotify playlist with the top songs from that date.

## Features
- Scrapes the Billboard Hot 100 chart for song titles on a given date.
- Searches for these songs on Spotify.
- Creates a private playlist on the user's Spotify account.
- Adds available songs to the playlist.

## Requirements
Before running the script, ensure you have the following installed:
- Python 3
- `requests`
- `beautifulsoup4`
- `spotipy`

You can install the required packages using:
```sh
pip install requests beautifulsoup4 spotipy
```

## Setup
1. **Spotify Developer Account**:
   - Create a Spotify Developer account at [Spotify Developer Dashboard](https://developer.spotify.com/).
   - Create an application and retrieve your `CLIENT_ID` and `CLIENT_SECRET`.
   - Set up a Redirect URI (e.g., `http://example.com`).

2. **Environment Variables**:
   - Set up environment variables for `CLIENT_ID` and `CLIENT_SECRET`:
   ```sh
   export CLIENT_ID='your_spotify_client_id'
   export CLIENT_SECRET='your_spotify_client_secret'
   ```

## Usage
Run the script and enter the date in `YYYY-MM-DD` format when prompted:
```sh
python script.py
```
### Example Workflow
1. The script asks for a date input.
2. It scrapes the Billboard Hot 100 chart for that date.
3. It searches for the songs on Spotify.
4. A new private playlist is created on your Spotify account.
5. Available songs are added to the playlist.

## Troubleshooting
- If songs are not found on Spotify, the search query may need modifications.
- If authentication fails, ensure your Spotify credentials are set correctly.
- If the Billboard website structure changes, update the BeautifulSoup selector.

## Notes
- The script requires user authentication with Spotify the first time it runs.
- Some songs might not be available on Spotify due to licensing issues.

## License
This project is licensed under the MIT License.

