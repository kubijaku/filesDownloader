import numpy
from bs4 import BeautifulSoup
from requests import get
import os
import requests


"""


"""

class Data:





    def saving_files(General_URL):
        allPaths = []
        allLinks = []

        page = get(General_URL)
        bs = BeautifulSoup(page.content,features="html.parser")

        for file in bs.find_all('div', class_='cmp-list-view__wrapper'):
            for link in file.find_all('a', class_='cmp-list-view__content download'):
                print(link.get('href'))
                allPaths.append(link.get('href'))
        for path in allPaths:
            string  = "https://pol.sika.com" + path
            allLinks.append(string)

        # Directory
        directory = General_URL.rsplit('/', 1)[-1]

        # Parent Directory path
        parent_dir = ""

        # Path
        path = os.path.join(parent_dir, directory)

        try:
            os.makedirs(path)
        except OSError as error:
            print(error)
        i = 0
        for URL in allLinks:
            i = i+1
            response = requests.get(URL)
            # 3. Open the response into a new file called instagram.ico
            fileName = directory + "/" + str(i) + ".pdf"
            open(fileName, "wb").write(response.content)



links = ['https://pol.sika.com/pl/budownictwo/chemia-pod-ogowa/kleje-parkietowe/kleje/sikabond-t-8.html',
         'https://pol.sika.com/pl/budownictwo/podlewki-i-zakotwienia/podlewki-cementowe/sikagrout-314.html',
         'https://pol.sika.com/pl/budownictwo/podlewki-i-zakotwienia/podlewki-cementowe/sikagrout-314.html',
         'https://pol.sika.com/pl/budownictwo/chemia-pod-ogowa/kleje-parkietowe/kleje/sikabond-t-8.html',
         'https://pol.sika.com/pl/budownictwo/materia-y-uszczelniajce/wype-niacze/sikaflex-11-fc.html',
         'https://pol.sika.com/pl/budownictwo/naprawa-betonu/systemy-naprawy-iochronybetonupcc/sika-repair-13-f.html',
         'https://pol.sika.com/pl/budownictwo/naprawa-betonu/systemy-naprawy-iochronybetonupcc/sika-monotop-620n.html',
         'https://pol.sika.com/pl/budownictwo/materia-y-uszczelniajce/uszczelniacze/sika-multiseal.html']

for link in links:
    Data.saving_files(link)

