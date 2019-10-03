import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

Peterson = 'https://washalert.sdsmt.edu/washalertweb/washalertweb.aspx?location=5013aaa2-fb4a-4f46-97f5-d6c4321a4f1d'
Palmerton = 'https://washalert.sdsmt.edu/washalertweb/washalertweb.aspx?location=76d93bb5-481a-468b-bfdb-45a891a4dd40'

def fullScrape(building):
    if building == 'Peterson':
        #open connection, grab the page
        uClient = uReq(Peterson)
        page_html = uClient.read()
        uClient.close()
    elif building == 'Palmerton':
        #open connection, grab the page
        uClient = uReq(Palmerton)
        page_html = uClient.read()
        uClient.close()
        

    #html parsing
    page_soup = soup(page_html, "html.parser")

    status_input = input('Desired status? ')
    if status_input == 'Available':
        #grabs each machine that is ready
        MachineList = page_soup.findAll("tr",{"class":"MachineReadyMode"}) + page_soup.findAll("tr",{"class":"MachineDoorOpenReadyMode"})
        
    elif status_input == 'End':
        #grabs finished machines
        MachineList = page_soup.findAll("tr",{"class":"MachineEndOfCycleMode"})
        
    elif status_input == 'Running':
        #grabs running machines
        MachineList = page_soup.findAll("tr",{"class":"MachineRunMode"}) + page_soup.findAll("tr",{"class":"MachineRunModeAlmostDone"})


    for machine in MachineList:
        text = machine.td.text

        status_container = machine.findAll("td", {"class":"status"})
        status = status_container[0].text

        time_container = machine.findAll("td", {"class":"time"})
        time = time_container[0].text

        print(text)
        print(status)
        print(time)
        
        print(' ')
