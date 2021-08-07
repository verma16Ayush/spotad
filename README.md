# Navigate around spotify ads

Here's a simple script that simply mutes your master audio
if spotify starts playing an ad. Then unmutes once the ad is
over. 

## Get Started
```bash
git clone https://www.github.com/verma16Ayush/spotad.git

pip install -r requirements.txt
```
### Setup a spotify app
1. Go to  https://developer.spotify.com/dashboard and sign in with your Spotify account.
2. Click on the `'CREATE AN APP'` option and provide an app name and app description as you'd like.
3. Go to `'EDIT SETTINGS'` and fill in the Redirect URIs placeholder with `http://localhost:8080/`, and click on Save.
4. Copy the `Client ID` and `Client Secret` and paste it in the corresponding placeholders in `'.env'` file.
5. Paste your spotify username in the username placeholder in `'.env'` file

## Run
Once above steps are done you can simply play music and run this in the background. Or better yet, make this script a daemon. Follow [this](https://stackoverflow.com/questions/1603109/how-to-make-a-python-script-run-like-a-service-or-daemon-in-linux)

---
Tested only on Ubuntu 20.04