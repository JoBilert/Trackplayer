import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty
import pygame
from pygame import mixer

tracks = [1,2,3]
volumes = []
class TrackscapeLayout(Widget):
    frame = ObjectProperty(None)
    sliders = ObjectProperty(None)
    info = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TrackscapeLayout, self).__init__(**kwargs)

    def add_Sliders(self):
        global tracks, volumes
        volumes = []
        for t in range(len(tracks)):
            volumes.append(self.sliders.add_widget(Slider(min=0,max=100, orientation='vertical')))




class Trackscape(App):
    def build(self):
        return TrackscapeLayout()



if __name__ == '__main__':
    Trackscape().run()
