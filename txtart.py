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
import subprocess
from time import sleep
from termcolor import colored, cprint
from pyfiglet import Figlet
from tabulate import tabulate

lol='lolcat'
tc='termcolor'
pf='pyfiglet'
te='tabulate'

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout =subprocess.DEVNULL, stderr =subprocess.STDOUT)

def loading():
    install_line = colored('Installing Packages', attrs=['bold'])
    print(install_line)
    animation = [
    "[        ]",
    "[=       ]",
    "[===     ]",
    "[====    ]",
    "[=====   ]",
    "[======  ]",
    "[======= ]",
    "[========]",
    "[ =======]",
    "[  ======]",
    "[   =====]",
    "[    ====]",
    "[     ===]",
    "[      ==]",
    "[       =]",
    "[        ]"
    ]

    notcomplete = True

    i = 0

    while notcomplete:
        print(colored(animation[i % len(animation)],'green', attrs=['bold','blink']), end='\r', flush=True)
        sleep(.05)
        i += 1
        if i == 16*2:
            break

def txtart():
    print('\n')

    print(colored(Figlet(font='3-d').renderText('TXTART'),'red', attrs=['bold','blink']))

    line1 = colored('Please type in 1 of the fonts above then hit Enter', attrs=['bold'])
    line2 = colored('Dont think to much they all look really cool ¯\_( ツ )_/¯', attrs=['bold', 'blink'])
    line3 = colored('For example the title "TXTart" above was written using the font 3-d\n', attrs=['bold'])
    line4 = colored('\nType in the text you want to be made into a masterpiece then hit Enter\n', attrs=['bold'])
    line5 = colored('\nType in a color that you would like yur text to be displayed in', attrs=['bold'])
    line6 = colored('The choices are: grey, red, green, yellow, blue, magenta, cyan, & white', attrs=['bold'])
    line7 = colored('For example the "TXTART" title was in red\n', attrs=['bold'])
    q_line = colored('\nAt any time feel free to type "quit" to exit TXTART', attrs=['bold'])
    font_line = colored('^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~FONTS~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~', attrs=['bold'])

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

    print(q_line)
    print(line1)
    print(line2)
    print(line3)
    font = input()

    if (font == 'quit' or font == 'q'):
        print(colored('\nThanks for trying it out anyway', attrs=['bold']))
        print(colored('(๑´╹‸╹`๑)', attrs=['bold']))
        quit()
    
    if not any(font in x for x in fonts):
        print(colored('\n┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻', attrs=['bold']))
        print(colored('Not A Font option', attrs=['bold']))
        print(colored('Try Again\n', attrs=['bold']))
        sleep(2.5)
        txtart()

    print(line4)
    text = input()

    print(line5)
    print(line6)
    print(line7)
    color = input()

    if (color == 'quit' or color == 'q'):
        print(colored('\nThanks for trying it out anyway', attrs=['bold']))
        print(colored('(๑´╹‸╹`๑)\n', attrs=['bold']))
        quit()
    elif not (color == 'grey' or color == 'red' or color == 'green' or color == 'yellow' or color == 'blue' or color == 'magenta' or color == 'cyan' or color == 'white'):
        print(colored('\n┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻', attrs=['bold']))
        print(colored('Not A Valid Color\n', attrs=['bold']))
        txtart()

    print('\n')
    print(colored(Figlet(font='%s' % font).renderText('%s' % text),'%s' %color, attrs=['bold','blink']))

    print(colored('\nWould you like to make more art??? (∩╹□╹∩)\n', attrs=['bold']))
    print(colored('Type "Y" for yes & "N" for no\n', attrs=['bold']))
    answer = input()
    
    if(answer == 'y' or answer == 'Y'):
        txtart()
    elif(answer == 'n' or answer == 'N'):
        quit()
    else:
        print(colored('\nI SAID ONLY TYPE Y OR N', attrs=['bold']))
        sleep(1)
        print(colored('\nCONGRATS YOU BROKE THE CODE\n', attrs=['bold']))
        sleep(1)
        print(colored('YOU MUST BE PUNISHED\n', attrs=['bold']))
        sleep(1)
        print(colored('''        +++++++++++++++++++++++++++oo++++oo+++++++++++++++++++++++++++y+os+++++++++++++o
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oy+so+++++++++++++o
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ss+y++++++++++++++o
        ++++++++++++++++++++++++++++++++++++++++++++++++++//:::::://+yo+y++++++++++++o++
        +++++++++++++++++++++++++++++++++++++++++++++/-.``          `--/s+++++++++++++++
        ++++++++++++++++++++++++++++++++++++++++++/:.`     ```....``````.:/+++++++++++++
        ++++++++++++++++++++++++++++++++++++++++/-.`    ``.--:::--....```.-:++++++++++++
        +++++++++++++++++++++++++++++++++++++++:-.`   `..--::::::----....-::/+++++++o++o
        ++++++++++++++++++++++++++++++++++o++/-.`   ``.--:::::::::::::::://+++++++ooo+++
        oooooooooooooooooooooooooooossssssss/..`   `..--::::::---::////++++ooooooooooooo
        +++++++++++++++++++++++oooooooooooo/.`````..-::::::::::::///+++++ooooshsoooooooo
        ++++++++++++++++++++++++++++++++++/-.``...-:::::::::::///++++oooosyhhdds++++++++
        ++++++++++++///////////:::::::::::--.---::///::::/:////+++++ooosyyhddmdo+++++++o
        ..----......`````````````````````.--::///////////////++++ooooosyhhddmmyo+++++ooo
        `      ```````````````..........--.-:::/+++++/+/++++oo+ooooossyhddmmNyo++++oooos
        ........----------::-:::::://://:---/--.-:/+oooooooooooosssssyddmmmNdo++++ooossy
        :::::::::///:/:://+/+++++++++++/::-.:/+//:-::+ossssssssosyyyhdmmmmdhoo++ooossyyy
        //////////+++++++++o+++oooooooo//+o/-.-/++/:://+ssssoossosydmmmmdhhhyoossssyyyyy
        //+++++++++++++++++++++oo++ooo++/-/ss/--:/oo+////+ssysoo//sdmmmmmmhdyssyyyyyyyyy
        +++++++oossysssoooo+++++//++++++/..-++/+/::/++//////syo::sddddddmmhhyyyyyyyyyyyy
        ++oooyhmNNNNNNNNmmmmddhyysooooo+o+/---::++//:::::::://+/+ydddmddddmmmddddddddddd
        ooshmNNNMMMMNNNNNNNNNNNNNNNNNNmms--/+++/:://::::/::::////ydddddddmNNNNmmmmmmmmmm
        yhddddmmNNNNNNMMMMMMMNNNNNNNNMMNs/---/o+/:---://////:////+hdmmmmNNNNNNNmmmmmmmmm
        hhddmmmNmmmdmmmNNMMMMMMMMMMMMMMMyo+o+::::-:://///////////+sdmNMNNNNNNNNNNmmmmmmm
        ddmmmmmNmmmmmdddddmmNMMMMMMMMMMMNyssyo//////////////////+sydmMMMMNNNNNNNNNNmmmmm
        mmmmmmNmmmmmmdddddddddmNNMMMMMMMMdhhhhyo++///+//////////+symMMMMMMMMMNNNNNNmmmmm
        NNNNNNNmmmmmmmmmmmmmmmmddmmNNMMMMmyyyhdyo++++++++////////osmMMMMMMMMMMMMMNNNNNmm
        NNNNNNNmNNNNNNMMMMMMNNNNNNNmNNNNNMmhddddhoosoooo++//+++/++oyMMMMMMMMMMMNNNNNNNNN
        mmmNNNNNNMMMNNNNNNNNNNMMMMMMMMMMNNNNNmmNNmysssooo++++++++++omMMMMMMMMMMNNNNNNNNN
        NNNNMMNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMmhsss+++ooo++++++odMMMMMMMMMMMMMMNNNN
        NNMMMNNNmmmmmmmmmmmmNNNNNNNNNNNMMMMMMMMMMMMMMmhyo++++oooooo+osmMMMMMMMNNNNNMMMMM
        NMMMMmmddddddddmmmmmNNNNNNNNNNNNNMMMMMMMMMMMMMNmhso++oooosssshdNNNNNNNNNNNNmNNNN
        MMMMmdddddddddddmmmmmmmmmmmmmNNNNNNNNNNNNNNNNNNNNhsooossyydmmNNNNNMMMMNNNNNNNNNN
        MMMNdddddddddddmmmmmmmmmmNNNNNNNNNNNNNNNNNNNNNmdmhhhyyhdmNNNNNNNmNNNNNNNNNNNNNNN
        MMNddhhdddddddmmmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNmNMmdmmNNNNNNNNNNNNNNNNNNNNNNNNNNN
        MNddhhdddddmmmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMNNNNNN
        MmddddddmmmmmmmmmNNNNNNNNNNmmmmNNNNNmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMNNNNNNNN
        NddddddmmmmmmmNNNNNNNNNNNNNNNNNNmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMM
        ddddmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNMMMMMMMMMM
        dmmmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNMMNNNMMMMM
        mmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMNNNNNNM
        mmdmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMNNNNNN\n\n''', attrs=['bold']))
        print(colored('SEE WHAT YOU MADE ME DO\n', attrs=['bold']))
        quit()
        

if __name__ == '__main__':
    loading()
    install(lol)
    install(tc)
    install(pf)
    install(te)
    txtart()
