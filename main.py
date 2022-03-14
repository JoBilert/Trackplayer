from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer


filename = ["chan1", "chan2", "chan3", "chan4", "chan5"]
bg_color = "black"
indcol = "red"
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)


# Funktionen
def browse_file(c, n):
    global filename
    fn = filedialog.askopenfilename()
    filename[c] = mixer.Sound(fn)
    filename[c].set_volume(0)
    tracks[c].set(fn)


def playtrack(event):
    global indcol
    temp = int(event.char)-1
    if filename[temp] != "chan1":
        filename[temp].play()
        indcol = "red"
        loops[temp].set("No Loop")
        loop_one.configure(bg=indcol)


def fade(event):
    global indcol
    temp = int(event.char)-1
    if filename[temp] != "chan1":
        filename[temp].fadeout(9000)
        indcol = "red"
        loops[temp].set("No Loop")
        loop_one.configure(bg=indcol)



def playLoop(event):
    global indcol
    temp = int(event.keysym)-1
    if filename[temp] != "chan1":
        filename[temp].play(-1)
        indcol = "green"
        loops[temp].set("Loop")
        loop_one.configure(bg=indcol)


def setVolume(value):
    for v in range(len(vol)):
        if filename[v-1] != ("chan"+str(v)):
            volume = int(vol[v].get())/100
            filename[v].set_volume(volume)


window = Tk()
window.geometry("1024x786")
window.title("Music Player")
window.configure(background = bg_color)

loops = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
tracks = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
vol = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]


# Text anzeigen
text = Label(window, text = "Trackplayer", font = ("Calibri", 20, "bold"),fg = "red", bg = bg_color)
text.pack()

# Rahmen für Tasten
frame = Frame(window, bg = bg_color)
frame.pack(padx=10, pady=10)

#LoadButtons
load_one = Button(frame, text="Load Track 1", command=lambda: browse_file(0, tracks))
load_one.grid(row=1, column=1, padx=10, pady=10)
load_two = Button(frame, text="Load Track 2", command=lambda: browse_file(1, tracks))
load_two.grid(row=1, column=2, padx=10, pady=10)
load_three = Button(frame, text="Load Track 3", command=lambda: browse_file(2, tracks))
load_three.grid(row=1, column=3, padx=10, pady=10)
load_four = Button(frame, text="Load Track 4", command=lambda: browse_file(3, tracks))
load_four.grid(row=1, column=4, padx=10, pady=10)
load_five = Button(frame, text="Load Track 5", command=lambda: browse_file(4, tracks))
load_five.grid(row=1, column=5, padx=10, pady=10)
load_six = Button(frame, text="Load Track 6", command=lambda: browse_file(5, tracks))
load_six.grid(row=1, column=6, padx=10, pady=10)

#filenames
file_one = Label(frame, textvariable=tracks[0])
file_one.grid(row=2, column=1, padx=10, pady=10)
file_two = Label(frame, textvariable=tracks[1])
file_two.grid(row=2, column=2, padx=10, pady=10)
file_three = Label(frame, textvariable=tracks[2])
file_three.grid(row=2, column=3, padx=10, pady=10)
file_four = Label(frame, textvariable=tracks[3])
file_four.grid(row=2, column=4, padx=10, pady=10)
file_five = Label(frame, textvariable=tracks[4])
file_five.grid(row=2, column=5, padx=10, pady=10)
file_six = Label(frame, textvariable=tracks[5])
file_six.grid(row=2, column=6, padx=10, pady=10)

# volume sliders
v_one = Scale(frame, from_=100, to=0, length=200, orient=VERTICAL, variable=vol[0], command=setVolume)
v_one.grid(row=3, column=1, padx=10, pady=10)
v_two = Scale(frame, from_=100, to=0, length=200, orient=VERTICAL, variable=vol[1], command=setVolume)
v_two.grid(row=3, column=2, padx=10, pady=10)
v_three = Scale(frame, from_=100, to=0, length=200, orient=VERTICAL, variable=vol[2], command=setVolume)
v_three.grid(row=3, column=3, padx=10, pady=10)
v_four = Scale(frame, from_=100, to=0, length=200, orient=VERTICAL, variable=vol[3], command=setVolume)
v_four.grid(row=3, column=4, padx=10, pady=10)
v_five = Scale(frame, from_=100, to=0, length=200, orient=VERTICAL, variable=vol[4], command=setVolume)
v_five.grid(row=3, column=5, padx=10, pady=10)
v_six = Scale(frame, from_=100, to=0, length=200, orient=VERTICAL, variable=vol[5], command=setVolume)
v_six.grid(row=3, column=6, padx=10, pady=10)


# loop indicators
loop_one = Label(frame, textvariable = loops[0])
loop_one.grid(row=4, column=1, padx=10, pady=10)
loop_two = Label(frame, textvariable = loops[1])
loop_two.grid(row=4, column=2, padx=10, pady=10)
loop_three = Label(frame, textvariable = loops[2])
loop_three.grid(row=4, column=3, padx=10, pady=10)
loop_four = Label(frame, textvariable = loops[3])
loop_four.grid(row=4, column=4, padx=10, pady=10)
loop_five = Label(frame, textvariable = loops[4])
loop_five.grid(row=4, column=5, padx=10, pady=10)
loop_six = Label(frame, textvariable = loops[5])
loop_six.grid(row=4, column=6, padx=10, pady=10)



# Statuszeile
statusbar = Label(window, text="Welcome to Trackplayer", relief=SUNKEN, anchor=W, font=("Calibri", 10, "italic"))
statusbar.pack(side=BOTTOM, fill = X)

window.bind('1', playtrack)
window.bind('<Control-KeyPress-1>', playLoop)
window.bind('<Alt-KeyPress-1>', fade)
window.bind('2', playtrack)
window.bind('<Control-KeyPress-2>', playLoop)
window.bind('<Alt-KeyPress-2>', fade)
window.bind('3', playtrack)
window.bind('<Control-KeyPress-3>', playLoop)
window.bind('<Alt-KeyPress-3>', fade)
window.bind('4', playtrack)
window.bind('<Control-KeyPress-4>', playLoop)
window.bind('<Alt-KeyPress-4>', fade)
window.bind('5', playtrack)
window.bind('<Control-KeyPress-5>', playLoop)
window.bind('<Alt-KeyPress-5>', fade)

window.mainloop()
