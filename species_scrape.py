import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
donatelink = 'https://act.biologicaldiversity.org/onlineactions/mLBxIVrBY0-PF8_oJWJbEw2?utm_expid=.QGpwm5uyRCWKJOr0upwtRQ.2&utm_referrer=https%3A%2F%2Fwww.biologicaldiversity.org%2F'
home = requests.get('https://www.biologicaldiversity.org/species/')
soup = BeautifulSoup(home.text, 'lxml')
mainlinks = soup.find(class_ = 'col cbd_content_main').find_all('a')
speclist = [spec.text for spec in mainlinks]
refs = ['https://www.biologicaldiversity.org/species/' + link['href'] for link in mainlinks]



def userprogram():
    for a, b in enumerate(speclist, 1):
        print("{}. {}".format(a, b))
    i = int(input('Which species would you like to explore? (1-7): '))
    page = requests.get(refs[i-1])
    soup2 = BeautifulSoup(page.text, 'lxml')
    speciesinfo = [paragraph.text for paragraph in soup2.find(class_= 'col cbd_content_main').find_all('p')]
    print(speclist[i-1])
    for info in speciesinfo:
        if len(info) > 5:
            print(info)
            print("-"*20)
        else:
            pass
    ii = input('Would you like a list of {} that you could help to save? (yes/no) '.format(speclist[i-1]))
    if ii.lower() == 'yes':
        species_page = soup2.find(class_='col-md-4 cbd_content_sidebar').find_all('a')
        creature_list = [(creature.text, 'https://www.biologicaldiversity.org/species/' + speclist[i-1].lower() + '/' + creature['href']) for creature in species_page if len(creature.text) > 2]
        for b,combo in enumerate(creature_list, 1):
            print('{}. {}'.format(b,combo[0].title()))
        print('Choose one to learn more (1-{}): '.format(len(creature_list)))
        iii = int(input(''))
        creature_site = requests.get(creature_list[iii-1][1])
        creature_soup = BeautifulSoup(creature_site.text, 'lxml')
        creature_summary = creature_soup.find(class_='col-md-6 cbd_content_left').find_all('p')
        creature_img_url = creature_soup.find(class_='banner').find('img')['src']
        imglink = 'https://www.biologicaldiversity.org/' + creature_img_url
        r = requests.get(imglink)
        specimg = Image.open(BytesIO(r.content))
        specimg.show()
        print('-'*20)
        print('Here\'s a pic of the {}'.format(creature_list[iii-1][0]))
        print('-'*20)

        for sec in creature_summary:
            print(sec.text)
            print('-'*20)
        print('The {} needs your help!  Click this link to donate: '.format(creature_list[iii-1][0]))
        print(donatelink)
        
userprogram()
 







