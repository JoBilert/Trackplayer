import os

import kivy
from kivy import platform
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy_garden.filebrowser import FileBrowser, get_home_directory
from tkinter import filedialog

import pygame
from pygame import mixer
tracks = []
volumes = []
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

class Files(Popup):
    def __init__(self, **kwargs):
        super(Files, self).__init__(**kwargs)




class TrackscapeLayout(Widget):
    frame = ObjectProperty(None)
    sliders = ObjectProperty(None)
    info = ObjectProperty(None)
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TrackscapeLayout, self).__init__(**kwargs)


    def filebrowser(self):
        fn = filedialog.askopenfilename()
        return fn

    def addSliders(self):
        global tracks, volumes
        for t in range(len(tracks)):
            volumes.append(self.sliders.add_widget(Slider(
                min=0,
                max=100,
                value=50,
                orientation='vertical',
                value_track=True,
                value_track_color=[1,0,0,1]))
            )

    def addTrack(self):
        tracks.append((mixer.Sound(self.filebrowser())))

class Trackscape(App):
    def build(self):
        return TrackscapeLayout()


if __name__ == '__main__':
    Trackscape().run()
