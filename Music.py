
import streamlit as st
import spotipy
import spotipy.oauth2 as oauth2
import lyricsgenius

# กำหนด Spotify API credentials
sp_client_id = 'ed4e37d603d34616ac82ad13e90acc56'
sp_client_secret = 'f1ea2627f5624711bbd2f40918a65f2a'
credentials = oauth2.SpotifyClientCredentials(client_id=sp_client_id, client_secret=sp_client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

# กำหนด Genius API key
genius = lyricsgenius.Genius('MJjsae9SougUeDtiZfWOVoJTIubxNlw9lIquh1LRhi2wIKq_l0LDNKVWBkElMAV2')

# สร้าง streamlit app
st.title('ค้นหาชื่อเพลง')
st.write('พิมพ์เนื่อเพลงที่ต้องการค้นหา')

# รับ input จากผู้ใช้
query = st.text_input('Search for a song or a part of its lyrics')

# ค้นหาเพลงจาก Spotify ด้วยเนื้อร้องบางส่วน
def search_spotify(query):
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['total'] > 0:
        track = results['tracks']['items'][0]
        return track
    else:
        return None

# ค้นหาเนื้อเพลงจาก Genius ด้วยชื่อเพลงและศิลปิน
#def search_genius(title, artist):
    #song = genius.search_song(title, artist)
    #return song

# แสดงผลการค้นหา
if st.button('Search'):
    #ค้นหาเพลงจาก Spotify
    track = search_spotify(query)
    if track:
        st.write(f"**{track['name']}** by {track['artists'][0]['name']} from the album {track['album']['name']}")
        # แสดงเนื้อเพลงจาก Genius
        #song = search_genius(track['name'], track['artists'][0]['name'])
        #if song:
            #st.write(song.lyrics)
        #else:
            #st.write('Lyrics not found on Genius.')
    else:
        st.write('Song not found on Spotify.')
