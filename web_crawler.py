import argparse
import os
import logging
import datetime
import urllib2

__version__ = "0.1.0"


DEBUG_FILE = None
KEYWORDS = "set"
LINK_INSIDE = []
LINK_OUTSIDE = []
SEARCH_LIST = []
FILE_TO_WRITE_PATH = ""
FILE_TO_READ_PATH = ""
WEBSITE = "https://docs.python.org/2/library/urllib2.html"#change back to None
USER_AGENT ="Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0" #change back to None


def main():

    set_debug_file()
    logging.debug(str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' set up the debug file')

    logging.debug(str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' calling get_commands')
    get_commands()

    html_code = get_html()
    # find_links_and_keywords(html_code)

    write_to_file(html_code)
    read_from_file()
    find_keywords()

    logging.debug(str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + ' end \n \n')


def set_debug_file():
    global DEBUG_FILE
    global FILE_TO_READ_PATH
    global FILE_TO_WRITE_PATH

    temp = os.getenv("HOME")
    temp2 = "/.mulvie/"
    temp3 = "web_cralwer/"
    filename = "log.txt"
    temp_file_name = "temp.txt"

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
    FILE_TO_READ_PATH = temp + temp2 + temp3 + temp_file_name
    FILE_TO_WRITE_PATH = temp + temp2 + temp3 + temp_file_name

    logging.basicConfig(filename=DEBUG_FILE, filemode='a', level=logging.DEBUG)


def get_html():
    header = {'User-Agent': USER_AGENT}
    req = urllib2.Request(WEBSITE, data=None, headers=header)

    html = urllib2.urlopen(req)
    html = html.read()
    return html


def find_links(html):
    global LINK_INSIDE
    global LINK_OUTSIDE

    try:
        from bs4 import BeautifulSoup
    except ImportError:
        logging.debug("Error")

    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a'):
        temp = link.get('href')
        # if needed to find out inside or outside
        LINK_INSIDE.append(temp)


def find_keywords():
    for word in SEARCH_LIST:
        if word == KEYWORDS:
            print "found !!!!!!"


def read_from_file():
    global SEARCH_LIST

    with open(FILE_TO_READ_PATH) as f:
        for line in f:
            temp = line.split("<")
            for line2 in temp:
                temp2 = line2.split(">")
                for line3 in temp2:
                    temp3 = line3.split(" ")
                    for line4 in temp3:
                        temp4 = line4.split("\n")
                        for line5 in temp4:
                            temp5 = line5.strip(" ")
                            SEARCH_LIST.append(temp5)

    print SEARCH_LIST
    print len(SEARCH_LIST)


def write_to_file(html):
    with open(FILE_TO_WRITE_PATH, 'w') as f:
        f.write(html)


def loop():
    pass


def get_commands():
    parser = argparse.ArgumentParser(version=__version__, description="a test server socket cli program")
    parser.add_argument('-i', '--input', action="store", help='path to text file with list of url to test')

    my_Arg = parser.parse_args()


if __name__ == '__main__':
    main()