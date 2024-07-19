from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import json
from collections import Counter
import sys
import glob
import numpy as np
from os import path
from PIL import Image, ImageOps
import os
import datetime
import random
import re

from app.classes import MyWordCloud
from app.config import swatch, STATIC_FOLDER, my_colour_func
import app.data

os.chdir('..')

def hsl_to_hex(h, s, l):
    import colorsys
    rgb = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))



def rank_simple(lst):
     return sorted(range(len(lst)), key=lst.__getitem__)

def produce(id, destination, maskfile):

    c = app.data.getdata(id)
 
    mask = np.array(Image.open(maskfile))
    stopwords={}
    wordcloud = WordCloud(width = 2000, height = 1200,
                    color_func=my_colour_func,
                    background_color = swatch('cream'), #'white',
                    mask=mask,
                    contour_color= swatch('ruby') # hsl_to_hex(0,100,30),
                    contour_width=20,
                    stopwords = stopwords,
                    relative_scaling = 0.45,
                    max_font_size = 350,
                    min_font_size = 10).generate_from_frequencies(c)

    wordcloud_image = wordcloud.to_image()

    border_color = swatch('ruby') # hsl_to_hex(0,100,30) 
    border_width = 5  
    bordered_image = ImageOps.expand(wordcloud_image,
                                     border=border_width,
                                     fill=border_color)

    plt.figure(figsize = (20, 12), facecolor = None)
    plt.imshow(bordered_image)
    plt.axis("off")
#    plt.title(f'{runner_id} - {runner_name} Runs: {len(data)} {pb} Events: {event_count}',
#            #y=0.5, 
#            loc='right',backgroundcolor='darkgreen',
#            rotation=0,color='white',
#            fontweight='bold',fontfamily='serif',fontsize='x-large')

    plt.savefig(f'{destination}/{id}.png')


if __name__ == '__main__':
    ids = [x.split('.')[0] for x in glob.glob('*.pkr')]
    ids = ['184594',]
    for i in ids:
#        produce(i, STATIC_FOLDER,'maskcrown.jpg')
        produce(i, STATIC_FOLDER,'maskparkrunlogo.jpg')
        print(f'Produced: {i} => {STATIC_FOLDER}/{i}.png')


