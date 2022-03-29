from yelpapi import YelpAPI
import argparse
from geopy.geocoders import Nominatim
import geocoder
from pprint import pprint
import json

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

#find location
g = geocoder.ip('me')
loc = g.address



#find a resturaunt
def findFood(cost):
    #find stores
    yelp_api = YelpAPI("rNgON3wacga5ckN2nuz12nvElvXtWEiWjAs-b1NYY29qW1kZ3XEtbiIZuVxWoRZqRJ_n-ktAPwmwVKcMlSC6cewuT1F6MnGJLWEwV_xNT1dOfmqT5Jqf_cSwh-9BYnYx")

    response = yelp_api.search_query(term='food', location=loc, limit=1, price=cost, open_now=True)


    #convert to usable data
    data = json.dumps(response)
    data2 = json.loads(data)

    def get_all_elements_in_list_of_lists(list):
        count = 0
        for element in list:
            count += len(element)

            if count == 2:
                info1 = element
        return info1

    l1 = list(data2.items())

    l2 = (get_all_elements_in_list_of_lists(l1))

    l3 = str(l2)

    l4 = list(l3.split(","))

    def getElements(list):
        count = 0
        for element in list:
            if count > 50 and count < 170:
                return element
            count += len(element)
        return count

    l5 = getElements(l4)

    l6 = str(l5)

    def split(word):
        return word.split()

    l7 = split(l6)
    print(l7)
    final = ""
    rejected = []

    for i in l7:
        if i == "name" or ":" in i:
            rejected.append(i)
        else:
            if "name" in final:
                final = ""
            final += i
            final += " "

    return final




#kivy
class Demo(MDApp):

    def build(self):
        screen = Screen()

        cheap= MDRectangleFlatButton(text="Cheap",pos_hint={'center_x':0.1,'center_y':0.5},on_release=self.price1)
        screen.add_widget(cheap)

        modest= MDRectangleFlatButton(text="Modest",pos_hint={'center_x':0.3,'center_y':0.5},on_release=self.price2)
        screen.add_widget(modest)

        expensive= MDRectangleFlatButton(text="Willing to spend a bit",pos_hint={'center_x':0.5,'center_y':0.5},on_release=self.price3)
        screen.add_widget(expensive)

        fancy= MDRectangleFlatButton(text="you are trying to impress someone",pos_hint={'center_x':0.8,'center_y':0.5},on_release=self.price4)
        screen.add_widget(fancy)



        return screen
    def price1(self,obj):
        print(findFood(1))

    def price2(self,obj):
        print(findFood(2))
    def price3(self,obj):
        print(findFood(3))
    def price4(self,obj):
        print(findFood(4))
if __name__=="__main__":
    Demo().run()
