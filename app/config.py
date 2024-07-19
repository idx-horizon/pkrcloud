import re
import random

STATIC_FOLDER = '/home/idx/pkr/static'

def get_themes():
  return {"default": 1}

def my_colour_func(word, font_size, position, orientation, random_state=None, **kwargs):

    color_weights = ['red'] * 6 +     \
                    ['green'] * 4 +   \
                    ['yellow'] * 2 +  \
                    ['blue'] * 2 +    \
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
