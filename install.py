import os
import urllib

font_path = "{0}/.fonts".format(os.getenv("HOME"))
font_list = ["Monaco_Linux.ttf", "aaaa", "dgsdfg"]


def download_fonts(filename):
    filename = urllib.urlretrieve("https://github.com/egorhm/dotfiles/blob/master/gitconfig", "testfile.txt")
    print(filename)


if __name__ == '__main__':
    print("--------------------------------------------------------------")
    print("Installing fonts")
    print("--------------------------------------------------------------")

    download_fonts()
