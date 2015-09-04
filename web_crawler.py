import argparse
import os
import logging
import datetime

__version__ = "0.1.0"


DEBUG_FILE = None

def main():

    set_debug_file()
    logging.debug(str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' set up the debug file')

    logging.debug(str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' calling get_commands')
    get_commands()

    logging.debug(str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' end \n \n')


def set_debug_file():
    global DEBUG_FILE

    temp = os.getenv("HOME")
    temp2 = "/.mulvie/"
    temp3 = "web_cralwer/"
    filename = "log.txt"

    t = temp + temp2
    tt = t + temp3

    if os.path.isdir(t):
        pass
    else:
        os.mkdir(t)

    if os.path.isdir(tt):
        pass
    else:
        os.mkdir(tt)

    DEBUG_FILE = temp + temp2 + temp3 + filename

    logging.basicConfig(filename=DEBUG_FILE, filemode='a', level=logging.DEBUG)


def get_commands():
    parser = argparse.ArgumentParser(version=__version__, description="a test server socket cli program")
    parser.add_argument('-i', '--input', action="store", help='path to text file with list of url to test', required=True)
    parser.add_argument('-o', '--output', action="store", help='path to text file to save results')
    parser.add_argument('-s', '--show', action="store_true", help='shows results at the end')
    parser.add_argument('-ver', '--verbose', action="store_true", help='Verbose ')##
    parser.add_argument('-u', '--user', action="store", help='change user agent ', required=True)


    my_Arg = parser.parse_args()


if __name__ == '__main__':
    main()