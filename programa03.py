# -*- coding: utf-8 -*-
"""
Created on Fri May 26 23:49:10 2023

@author: Lucas
"""

# https://youtu.be/bojtukutqe0  


from pytube import YouTube

yt = YouTube('https://youtu.be/bojtukutqe0')

#print(yt.title)
#print(yt.thumbnail_url)

for video in yt.streams.filter(file_extension="mp4"):
    print(video)


v = yt.streams.get_by_itag(160)
v.download()
