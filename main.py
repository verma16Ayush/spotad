'''
अभी अभी दिल की सुनी है.
अभी ना करो ज़माने की बात.

अभी अभी बातें रुकी हैं.
अभी अभी दोहराने की बात.
'''


from requests.sessions import default_headers
import spotipy
from spotipy import util
import time
from dotenv import dotenv_values
# import alsaaudio
from subprocess import call

def Mute() -> None:
    call(["amixer", "-D", "pulse", "sset", "Master", "0%"])

def Unmute(vol:int) -> None:
    call(["amixer", "-D", "pulse", "sset", "Master", "{}%".format(vol)])

def setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI):
    token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)
    return spotipy.Spotify(auth=token)

def main(username, scope, clientID, clientSecret, redirectURI, default_vol) -> None: 
    # vol = mixer.getvolume()
    vol = default_vol
    spotify = setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI)
    flag = 0

    while True:
        
        try:
            current_track = spotify.current_user_playing_track()
            # print(current_track)
        except:
            print('token expired')
            spotify = setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI)
            current_track = spotify.current_user_playing_track()
            
        try:
            if current_track['currently_playing_type'] == 'ad' and not flag:
                Mute()
                flag = 1
                print('Muting for the duration of advertisement')
            elif current_track['currently_playing_type'] != 'ad' and flag:
                flag = 0
                print("unmuting")
                Unmute(vol)
        except TypeError:
            print(TypeError)
        
        time.sleep(1)

if __name__ == '__main__':
    
    # mixer = alsaaudio.Mixer()
    variables = dotenv_values(".env")
    spotifyUsername = variables["USERNAME"]
    spotifyClientID = variables["CLIENT_ID"]
    spotifyClientSecret = variables["CLIENT_SECRET"]
    default_vol = int(variables["DEFAULT_VOL"])
    spotifyAccessScope = "user-read-currently-playing"
    spotifyRedirectURI = "http://localhost:8080/"
    main(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret, spotifyRedirectURI, default_vol)