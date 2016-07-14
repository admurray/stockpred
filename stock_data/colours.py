'''
Filename        : colours.py
Author          : Aditya Murray 
Date            : July 6, 2016
Description     : This is a utility class to provide a neat way to write
                  coloured texts
'''

import random

#======== TEXT FORMATTING ==========================

def normal_text(text):
    return ("\033[0;37;40m%s" %text)

def underlined_text(text):
    return ("\033[2;37;40m%s\033[0m" %text)

def bright_colour(text):
    return ("\033[1;37;40m%s\033[0m" %text)

def negative_colour(text):
    return ("\033[3;37;40m%s\033[0m" %text)

#============= COLOURED TEXT ========================

def dark_gray(text):
    return ("\033[1;30;40m%s\033[0m" %text)

def bright_red(text):
    return ("\033[1;31;40m%s\033[0m" %text)

def bright_green(text):
    return ("\033[1;32;40m%s\033[0m " %text)

def yellow(text):
    return ("\033[1;33;40m%s\033[0m" %text)

def bright_blue(text):
    return ("\033[1;34;40m%s\033[0m" %text)

def bright_magenta(text):
    return ("\033[1;35;40m%s\033[0m" %text)

def bright_cyan(text):
    return ("\033[1;36;40m%s\033[0m" %text)

def white(text):
    return ("\033[1;37;40m%s\033[0m" %text)

def holi_hai(text):
    wl = list(text)
    temp_start = '\033[1;'
    temp_end = '\033[0m'
    text2 = ''
    print wl
    for each in wl:
        ran1 = random.randint(30, 55)
        ran2 = random.randint(40, 59)
        text2 += '%s%s;%sm%s%s'%(temp_start, ran1, ran2, each, temp_end)
    return text2
#================ COLOUR ON GREY =================
def black_on_grey(text):
    return ("\033[0;30;47m%s\033[0m" %text)

def red_on_grey(text):
    return ("\033[0;31;47m%s\033[0m" %text)

def green_on_grey(text):
    return ("\033[0;32;47m%s\033[0m"%text)

def yellow_on_grey(text):
    return ("\033[0;33;47m%s\033[0m"%text)

def blue_on_grey(text):
    return ("\033[0;34;47m%s\033[0m"%text)

def magenta_on_grey(text):
    return ("\033[0;35;47m%s\033[0m" %text)

def cyan_on_grey(text):
    return ("\033[0;36;47m%s\033[0m"%text)

def light_grey_on_grey(text):
    return ("\033[0;37;40m%s\033[0m" %text)

#=============== WHITE ON COLOUR ==================
def white_on_red(text):
    return ("\033[0;37;41m%s\033[0m" %text)

def white_on_green(text):
    return ("\033[0;37;42m%s\033[0m" %text)

def white_on_yellow(text):
    return ("\033[0;37;43m%s\033[0m" %text)

def white_on_blue(text):
    return ("\033[0;37;44m%s\033[0m" %text)

def white_on_magenta(text):
    return ("\033[0;37;45m%s\033[0m" %text)

def white_on_cyan(text):
    return ("\033[0;37;46m%s\033[0m" %text)

def white_on_grey(text):
    return ("\033[0;37;47m%s\033[0m" %text)

def white_on_black(text):
    return ("\033[0;37;48m%s\033[0m" %text)
#=====================


s = "All the worlds a stage and we are all idiots who think we are awesome"
print holi_hai(s)
