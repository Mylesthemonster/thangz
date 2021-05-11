# ░█████╗░██████╗░███████╗░█████╗░████████╗███████╗██████╗░  ██████╗░██╗░░░██╗
# ██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝
# ██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░█████╗░░██║░░██║  ██████╦╝░╚████╔╝░
# ██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██╔══╝░░██║░░██║  ██╔══██╗░░╚██╔╝░░
# ╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░███████╗██████╔╝  ██████╦╝░░░██║░░░
# ░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░

# ███╗░░░███╗██╗░░░██╗██╗░░░░░███████╗░██████╗  ░░░░░██╗░█████╗░██╗░░██╗███╗░░██╗░██████╗░█████╗░███╗░░██╗
# ████╗░████║╚██╗░██╔╝██║░░░░░██╔════╝██╔════╝  ░░░░░██║██╔══██╗██║░░██║████╗░██║██╔════╝██╔══██╗████╗░██║
# ██╔████╔██║░╚████╔╝░██║░░░░░█████╗░░╚█████╗░  ░░░░░██║██║░░██║███████║██╔██╗██║╚█████╗░██║░░██║██╔██╗██║
# ██║╚██╔╝██║░░╚██╔╝░░██║░░░░░██╔══╝░░░╚═══██╗  ██╗░░██║██║░░██║██╔══██║██║╚████║░╚═══██╗██║░░██║██║╚████║
# ██║░╚═╝░██║░░░██║░░░███████╗███████╗██████╔╝  ╚█████╔╝╚█████╔╝██║░░██║██║░╚███║██████╔╝╚█████╔╝██║░╚███║
# ╚═╝░░░░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░  ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░╚══╝

import sys
from termcolor import colored, cprint
from pyfiglet import Figlet
from tabulate import tabulate

def txtart():
    print('\n')
    print(colored(Figlet(font='banner3-D').renderText(' TXT ART '),'magenta', attrs=['bold','blink']))

    line1 = colored('\n Please type in 1 of the fonts above then hit Enter \n', 'red', attrs=['reverse', 'blink'])
    line2 = colored(' Dont think to much they all look really cool ( ͡° ͜ʖ ͡°) \n', 'yellow', attrs=['reverse', 'blink'])
    line3 = colored(' For example the title "TXTart" above was written using the font banner3-D \n', 'green', attrs=['reverse', 'blink'])
    line4 = colored('\n Type in the text you want to be made into a masterpiece then hit Enter \n', 'cyan', attrs=['reverse', 'blink'])
    line5 = colored('\n Type in a color that you would like yur text to be displayed in \n', 'blue', attrs=['reverse', 'blink'])
    line6 = colored(' The choices are: grey, red, green, yellow, blue, magenta, cyan, & white \n', 'magenta', attrs=['reverse', 'blink'])
    line7 = colored(' For example Fonts was in magenta \n', 'white', attrs=['reverse', 'blink'])
    font_line = colored('^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~FONTS~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~', 'grey', attrs=['bold', 'blink'])

    print(font_line)
    fonts = [['3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet'],
            ['avatar', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic'],
            ['bell', 'big', 'bigchief', 'binary', 'block', 'bubble', 'bulbhead'],
            ['calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'computer'],
            ['contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge'],
            ['cybermedium', 'cybersmall', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix'],
            ['drpepper', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwater'],
            ['epic', 'fender', 'fourtops', 'fuzzy' , 'goofy', 'gothic', 'graffiti'],
            ['hollywood', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic'],
            ['ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban', 'larry3d', 'lcd'],
            ['lean', 'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour'],
            ['mike', 'mini', 'mirror', 'mnemonic', 'morse', 'moscow', 'nancyj-fancy'],
            ['nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre', 'pawp'],
            ['peaks', 'pebbles','pepper', 'poison', 'puffy', 'pyramid', 'rectangles'],
            ['relief', 'relief2', 'rev', 'roman', 'rot13', 'rounded', 'rowancap'],
            ['rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap', 'shadow'],
            ['shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1'],
            ['smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello'],
            ['standard', 'starwars', 'stellar', 'stop', 'straight', 'tanja', 'tengwar'],
            ['term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tinker-toy'],
            ['tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'wavy', 'weird']]

    print(tabulate(fonts))

    print(line1)
    print(line2)
    print(line3)
    font = input()

    print(line4)
    text = input()

    print(line5)
    print(line6)
    print(line7)
    color = input()

    if not (color == 'grey' or color == 'red' or color == 'green' or color == 'yellow' or color == 'blue' or color == 'magenta' or color == 'cyan' or color == 'white'):
        print('┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻')
        print('Not A Valid Color')
        quit()

    print('\n')
    print(colored(Figlet(font='%s' % font).renderText('%s' % text),'%s' %color, attrs=['bold','blink']))

if __name__ == '__main__':
  txtart()
