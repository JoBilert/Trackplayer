from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer

# Variables
counter = 1
bg_color = "black"
indcol = ["red", "green"]
tracks = []
volume = []

# Run mixer
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)


# Track-Class
class Track:
    def __init__(self, file):
        global counter
        self.sound = mixer.Sound(file)
        self.sound.set_volume(0.5)
        self.soundLoop = False
        self.soundPlay = False
        T.insert(END, 'Track added:\n')
        T.insert(END, (str(counter) + "-" + file))
        counter += 1

    def playTrack(self, event):
        self.sound.play()
        self.soundPlay = True

    def playLoop(self, event):
        self.sound.play(-1)
        self.soundPlay = True
        self.soundLoop = True

    def setVolume(self, value):
        test = float(value) / 100
        print(test)
        self.sound.set_volume(test)

    def fade(self, event):
        self.sound.fadeout(5000)
        self.soundPlay = False
        self.soundLoop = False


# File select
def browse_file():
    fn = filedialog.askopenfilename()
    return fn

# Adds Volumesliders and Hotkey-Control
def add():
    global volume, tracks, frame
    volume = []
    vol = []
    a = IntVar()
    for t in range(len(tracks)):
        volume.append(Scale(frame, from_=100, to=0, length=200, orient=VERTICAL, variable=vol.append(a),
                            command=tracks[t].setVolume))
        volume[t].grid(row=3, column=(t + 1), padx=10, pady=10)
        # add hotkeys
        window.bind(str(t + 1), tracks[t].playTrack)
        window.bind('<Control-KeyPress-' + str(t + 1) + '>', tracks[t].playLoop)
        window.bind('<Alt-KeyPress-' + str(t + 1) + '>', tracks[t].fade)

# Main Program
window = Tk()
window.geometry("1024x786")
window.title("Music Player")
window.configure(background=bg_color)

# Headline
text = Label(window, text="Trackplayer", font=("Calibri", 20, "bold"), fg="red", bg=bg_color)
text.pack()

# Frames
frame = Frame(window, bg=bg_color)
frame.pack(padx=10, pady=10)
frame2 = Frame(window, relief=SUNKEN)
frame2.pack(side="bottom", padx=10, pady=10, fill=X)

# AddTrack
addTrack = Button(frame, text="Add Track", command=lambda: tracks.append(Track(browse_file())))
addTrack.grid(row=1, column=1, padx=10, pady=10)

# volume sliders
addSliders = Button(frame, text="Add Volume Sliders", command=lambda: add())
addSliders.grid(row=1, column=2, padx=10, pady=10)

# LogBox
S = Scrollbar(frame2)
T = Text(frame2, height=10)
S.pack(side="right", fill=Y)
T.pack(side="left", fill="both")

# Status
statusbar = Label(window, text="Welcome to Trackplayer", relief=SUNKEN, anchor=W, font=("Calibri", 10, "italic"))
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()
