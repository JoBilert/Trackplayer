from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer

# Variables
counter = 1
bg_color = "black"
indcol = "red"
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
        replay_vol = float(value) / 100
        self.sound.set_volume(replay_vol)

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
    global volume, tracks, slframe
    vol = []
    frames = []
    a = IntVar()

    # remove existing sliders
    if len(volume) > 0:
        for t in range(len(tracks)):
            volume[t-1].pack_forget()

    # add a slider for each loaded track
    for t in range(len(tracks)):
        frames.append(Frame(slframe, border="3px", relief=SUNKEN))
        frames[t].pack(side=LEFT, padx=5)
        volume.append(Scale(frames[t], from_=100, to=0, length=200, orient=VERTICAL, variable=vol.append(a), command=tracks[t].setVolume))
        volume[t].pack(side=LEFT)

        # add hotkeys for each track
        window.bind(str(t + 1), tracks[t].playTrack)
        window.bind('<Control-KeyPress-' + str(t + 1) + '>', tracks[t].playLoop)
        window.bind('<Alt-KeyPress-' + str(t + 1) + '>', tracks[t].fade)


# Main Program
window = Tk()
window.geometry("1024x786")
window.title("TrackPlayer")
window.resizable(True, True)
window.maxsize(window.winfo_screenwidth(), window.winfo_screenheight()-100)

# Headline
text = Label(window, text="Trackplayer", font=("Calibri", 20, "bold"), fg="red")
text.pack()

# Frame for buttons and sliders
topframe = Frame(window, width=window.winfo_reqwidth())
topframe.pack(fill=X)
# Button subframe
bframe = Frame(topframe)
bframe.pack(side=TOP, padx=10, pady=10)
# Sliders subframe
slframe = Frame(topframe)
slframe.pack(side=LEFT, padx=10, pady=10)
# Frame for Logbox and Statusbar
stframe = Frame(window, relief=SUNKEN)
stframe.pack(side="bottom", padx=10, pady=10, fill=X)


# AddTrack
addTrack = Button(bframe, text="1. Add Track(s)", command=lambda: tracks.append(Track(browse_file())))
addTrack.pack(pady=5)

# volume sliders
addSliders = Button(bframe, text="2. Add Volume Slider(s)", command=lambda: add())
addSliders.pack(pady=5)

# LogBox
console = Frame(stframe)
console.pack(side=TOP, fill=X, pady=2)
S = Scrollbar(console, width=20)
T = Text(console, width=window.winfo_reqwidth()-20, height=10)
S.pack(side=RIGHT, fill=Y)
T.pack()

# Status
statusbar = Label(stframe, text="Welcome to Trackplayer", relief=SUNKEN, anchor=W, font=("Calibri", 10, "italic"))
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()
