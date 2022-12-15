import csv
import mudopy
from selenium.webdriver.common.by import By
import spotdl


def readfile():
    with open('spotify.csv', encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            # print (row)
            pass


def downloadmusic():
    mudopy.download_path("E:\AIProjectFrontEnd\music")
    mudopy.download("Rich Flex")


def main():
    downloadmusic()


main()
