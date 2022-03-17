# Trackplayer
Multi-Track music.player with loop and fadeout function.

The player is meant to be a highly customizable soundboard.

## Usage
After starting the python program you are presented with the main window:

<img width="770" alt="image" src="https://user-images.githubusercontent.com/8271443/158754553-5eb76f60-a42b-457b-8f64-18130ed0f663.png">

Use the button "1. Add Track(s)" to add audio files (pygame mixer officially supports **ogg** and **uncompressed wav**, but I have encountered no problems with **mp3** so far either).
The logbox at the bottom of the windows will show you the number of the track and the file loaded into the track.

<img width="770" alt="image" src="https://user-images.githubusercontent.com/8271443/158756477-6456cc69-e4b6-4084-b4db-157376e0d8df.png">

*As the tracks are mapped to the number-keys you are limited to 10 tracks max for now!*

When you are finished loading your tracks, click the "2. Add Volume Slider(s)" button and a number of volume slider according to the number of loaded tracks will appear in the center of the window.

<img width="770" alt="image" src="https://user-images.githubusercontent.com/8271443/158758375-907e8999-a5b8-41bf-9036-3f1e412a2776.png">

*You can later add tracks by using the "1. Add Track(s)" button AND the "2. All Volume Slider(s)" again at any time.

Once all your tracks and volume sliders are loaded you have three options:
1. Start playing a track -> Press the number key of the track on your keyboard.
2. Start playing a track in a loop -> Press *CTRL + Numberkey of track*
3. Fade track out in 5 seconds and stop -> Press *Alt + Numberkey of track*

## TODO
* add option for setting fadeout-time
* add ability to resort tracks after loading
* add ability to remove a certain track from list
* add ability to insert a track at a certain place in the list
* facelift
* Android version
