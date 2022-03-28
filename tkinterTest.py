from yelpapi import YelpAPI
import argparse
from geopy.geocoders import Nominatim
import geocoder
from pprint import pprint
import json
import tkinter as tk


root = tk.Tk()
root.wm_geometry("500x500")
root.title('find food')

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="news")


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

    print(l5)

    return l5



button = tk.Button(frame, text='Enter', command=lambda: findFood(1))
button.pack()

root.mainloop()
