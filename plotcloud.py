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

STATIC_FOLDER = './pkr/static'

def hsl_to_hex(h, s, l):
    import colorsys
    rgb = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

def weighted_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # Weights for colors: red is more likely to be chosen
    color_weights = ['red'] * 8 + ['green'] * 5 + ['yellow'] * 2 + ['black'] * 2
    chosen_color = random.choice(color_weights)
    if word in ['2010','2011','2012','2013','2014','2015','2016','2017','2018',
                '2019','2020','2021','2022','2023','2024']:
        chosen_color ='black'

    if chosen_color == 'red':
        return "hsl(0, 100%, {}%)".format(random.randint(20, 40))
    elif chosen_color == 'green':
        return "hsl(100, 100%, {}%)".format(random.randint(20, 35))
    elif chosen_color == 'yellow':
        return "hsl(50, 100%, {}%)".format(random.randint(20, 40))
    elif chosen_color == 'black':
        return "hsl(0,0%,0%)"

def getdata(id):
    print(id)
    with open(f'{id}.pkr','r',encoding='utf-8') as f:
        data = json.loads(f.read())
        event_count = len(set([x['Event'] for x in data[1]['runs']]))
        return data[1]['runs'], data[1]['title'], event_count

def convert_to_seconds(tm):
    if len(tm) > 5:
        return int(sum([float(a)*float(b) for a,b in zip(tm.split(':'),[3600,60,1])]))
    else:
        return int(sum([float(a)*float(b) for a,b in zip(tm.split(':'),[60,1])]))

def rank_simple(lst):
     return sorted(range(len(lst)), key=lst.__getitem__)

def produce(id, destination, maskfile):

    data, title, event_count = getdata(id)
    c = Counter([x['Event'] for x in data])

    c[f'Events: {event_count}'] =  10

    yrc = Counter()
    #c.update([x['Run Date'][-4:] for x in data])
    for yr in [x['Run Date'][-4:] for x in data]:
        c[yr]=9
    yrc.update([x['Run Date'][-4:] for x in data])
    #print(yrc)
    #print(rank_simple(yrc))

    runner_id = f"A{id}"
    runner_name = f"{title[:title.index(' ')]}"
    c[runner_name] = min(11, len(data))
    c[runner_id] = min(12, len(data))
    c[f'Runs:{len(data)}'] = min(12, len(data))

    pbsecs = min([convert_to_seconds(x['Time']) for x in data])
    pb = 'PB: ' + str(datetime.timedelta(seconds=pbsecs))[-5:]
    c[pb] = min(12, len(data))

    print(runner_id, runner_name, pb)

    mask = np.array(Image.open(maskfile))
    stopwords={}
    wordcloud = WordCloud(width = 2000, height = 1200,
                    color_func=weighted_color_func,
                    background_color ='white',
                    mask=mask,
                    contour_color=hsl_to_hex(0,100,30),   # 'darkgreen',
                    contour_width=20,
                    stopwords = stopwords,
                    relative_scaling = 0.45,
                    max_font_size = 350,
                    min_font_size = 10).generate_from_frequencies(c)

    wordcloud_image = wordcloud.to_image()

    border_color = hsl_to_hex(0,100,30) 
    border_width = 5  # Adjust the border width as needed
    bordered_image = ImageOps.expand(wordcloud_image,
                                     border=border_width,
                                     fill=border_color)

    plt.figure(figsize = (20, 12), facecolor = None)
    plt.imshow(bordered_image)
    plt.axis("off")
    plt.title(f'{runner_id} - {runner_name} Runs: {len(data)} {pb} Events: {event_count}',
            #y=0.5, 
            loc='right',backgroundcolor='darkgreen',
            rotation=0,color='white',
            fontweight='bold',fontfamily='serif',fontsize='x-large')

    plt.savefig(f'{destination}/{id}.png')


if __name__ == '__main__':
    ids = [x.split('.')[0] for x in glob.glob('*.pkr')]
    ids = ['184594',]
    for i in ids:
#        produce(i, STATIC_FOLDER,'maskcrown.jpg')
        produce(i, STATIC_FOLDER,'maskparkrunlogo.jpg')
        print(f'Produced: {i} => {STATIC_FOLDER}/{i}.png')


