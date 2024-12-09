#!/usr/bin/python


from font_list import fonts
from pyfiglet import Figlet
import random
import sys


def main() :
    # check for CLA
    if len(sys.argv) == 2 :
        sys.exit("Usage: ./figlet.py or ./figlet.py -f font_name or ./figlet.py --font font_name")
    elif len(sys.argv) > 3 :
        sys.exit("Usage: ./figlet.py or ./figlet.py -f font_name or ./figlet.py --font font_name")
    elif sys.argv[1] != "--font" and sys.argv[1] != "-f" :
        sys.exit("Usage: ./figlet.py or ./figlet.py -f font_name or ./figlet.py --font font_name")

    # assign font
    font_var = None
    if len(sys.argv) == 1 : font_var = fonts[random.randrange(0, 147)]
    else : 
        try : font_var = fonts[fonts.index(sys.argv[2])]
        except : sys.exit("No such font found")

    # get input from user and format the output
    inpt = input("Input: ")
    font_obj = Figlet(font=font_var)
    print(font_obj.renderText(inpt))
        

if __name__ == "__main__" :
    main()
