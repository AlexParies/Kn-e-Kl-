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


#find location
g = geocoder.ip('me')
print(g.latlng)
print(g.address)

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

    return l5



#kivy

class LoginScreen(GridLayout):



    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        def foodFinder(price):
            print(findFood(price))
        self.cols = 2
        self.cheap = Button(text = "Cheap")
        self.cheap.bind(on_press= foodFinder(1))
        self.add_widget(self.cheap)
        self.modest = Button(text = "Modest")
        self.add_widget(self.modest)
        self.fancy = Button(text = "Trying to impress someone")
        self.add_widget(self.fancy)
        self.rich = Button(text = "Im worth more than 90% of the population")
        self.add_widget(self.rich)


class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
