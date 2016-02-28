import os
import urllib
from subprocess import call

font_path = "{0}/.fonts".format(os.getenv("HOME"))
# font_list = ["Monaco-Linux.ttf", "Menlo-Regular.ttf"]
font_list = ["Inconsolata.otf"]
url = "https://github.com/egorhm/linux-fonts/raw/master/fonts"


def download_font(filename):
    dwn_url = "{0}/{1}".format(url, filename)
    local_path = "{0}/{1}".format(font_path, filename)
    localname = urllib.urlretrieve(dwn_url, local_path)
    return localname


def install():
    if not os.path.exists(font_path):
        print("{0} doesn't exist and will be created".format(font_path))
        os.makedirs(font_path)
        print("dir created")

    for filename in font_list:
        font_file = download_font(filename)
        print("{0} downloaded to {1}".format(filename, font_file))

    print("calling fc-cache...")
    call(["fc-cache"])


if __name__ == '__main__':
    print("--------------------------------------------------------------")
    print("Installing fonts")
    print("github: https://github.com/egorhm/linux-fonts")
    print("--------------------------------------------------------------\n")
    install()
    print("\n--------------------------------------------------------------")
    print("Fonts installed")
    print("--------------------------------------------------------------")
