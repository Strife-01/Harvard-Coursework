#!/usr/bin/python
import re
import sys


def main() :
    try : fname = sys.argv[1]
    except : quit('NO_FILE_NAME')

    extension = re.findall('.*(\..*)$', fname)
    f_type = e_type(extension[0])
    
    print(f_type)


def e_type(extension) :
    match extension :
        case '.gif' : return 'image/gif'
        case '.jpg' : return 'image/jpg'
        case '.jpeg' : return 'image/jpeg'
        case '.png' : return 'image/png'
        case '.pdf' : return 'application/pdf'
        case '.txt' : return 'text/plain'
        case '.zip' : return 'application/zip'
        case _ : return 'application/octet-stream'


main()
