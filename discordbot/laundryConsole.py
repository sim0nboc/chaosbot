import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

from washAlertScrape import *

building = input('What building? ')
MachineList = fullScrape(building)


        

