#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul 28th 2017

@author: yannickleroux

The purpose of this program is to parse the traxsource website
and try to find zippyshare download links for the charted tracks.

"""
from bs4 import BeautifulSoup
import re
import requests
import webbrowser


url = input("Traxsource chart URL: ")
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
results_page = BeautifulSoup(response.content, 'lxml')

indiv_tracks = results_page.findAll('div', {'class':'ttib info'})

tracklist = []

for track in indiv_tracks:
    title = track.find('a', {'class':'com-title'}).get_text()
    artist = track.find('a', {'class':'com-artists'}).get_text()
    track_text = re.sub('[^A-Za-z0-9]+', ' ', artist + ' '+ title).lstrip() # strip from non apha
    tracklist.append(track_text)

for item in tracklist:
    new = 2
    tabUrl = "http://google.com/search?q="
    term = item + "+zippyshare" # searching for matching zippyshare link
  
    webbrowser.open(tabUrl + term,new = new)

        
