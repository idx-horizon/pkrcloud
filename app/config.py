import re
import random
import colorsys

STATIC_FOLDER = '/home/idx/pkr/static'

def get_themes():
  return {"default": 1}

def hsl_to_hex(h, s, l):
    rgb = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))



def swatch(c):
  colours = {
    'cream': hsl_to_hex(30,100,96),
    'ruby':  hsl_to_hex(0,100,30)
  }
  
  return colours[c]  

def my_colour_func(word, font_size, position, orientation, random_state=None, **kwargs):

    color_weights = ['red'] * 5 +     \
                    ['green'] * 5 +   \
                    ['yellow'] * 5 +  \
                    ['blue'] * 5 +    \
                    ['black'] * 0
                    
    chosen_color = random.choice(color_weights)
  
    # 4 digit numbers, e.g. 2012, 2023
    if re.match(r'^\d{4}$',word):   
        chosen_color ='black'

    if chosen_color == 'red':
        return "hsl(0, 100%, {}%)".format(random.randint(20, 40))
    elif chosen_color == 'green':
        return "hsl(100, 100%, {}%)".format(random.randint(20, 35))
    elif chosen_color == 'yellow':
        return "hsl(50, 100%, {}%)".format(random.randint(20, 40))
    elif chosen_color == 'blue':
        return "hsl(250, 100%, {}%)".format(random.randint(20, 40))        
    elif chosen_color == 'black':
        return "hsl(0,0%,0%)"
