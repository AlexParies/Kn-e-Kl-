#to setup use the command "pip install -r requirements.txt"
from yelpapi import YelpAPI
import argparse
from geopy.geocoders import Nominatim
import geocoder
from pprint import pprint
import json
import webbrowser

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import random as randy

class ButtonWindow(Screen):
    pass

class ResultWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("honkwindow.kv")

class No_Clue(App):
    global link
    link = ""
    global final
    final = ""

    def FindFood(self, cost):
        global link
        global final
        g = geocoder.ip('me')
        loc = g.address
        link = "https://www.google.com/maps/search/"

        yelp_api = YelpAPI("rNgON3wacga5ckN2nuz12nvElvXtWEiWjAs-b1NYY29qW1kZ3XEtbiIZuVxWoRZqRJ_n-ktAPwmwVKcMlSC6cewuT1F6MnGJLWEwV_xNT1dOfmqT5Jqf_cSwh-9BYnYx")

        response = yelp_api.search_query(price=cost,term='restaurants', location=loc, limit=30,  open_now=True)

        #convert to usable data
        data = json.dumps(response, indent=4)
        data2 = json.loads(data)
        x = response.get("businesses")
        num = 1
        names = []
        for i in x:
            num += 1
            x2 = i.get("name")
            names.append(x2)
        final = randy.choice(names)
        link+=final
        #print(final)
        return final

    def OpenLink(self):
        #print("Link Opened")
        #print(link)
        webbrowser.open(link)

    def build(self):
        return kv


if __name__=="__main__":
    No_Clue().run()
