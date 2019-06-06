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
    misc = input('whats your favorite animal,kangaroos...cats...otters?')
    print(misc.upper() + '?!!? MADAM/SIR THEY ARE ENDANGERED. PLS HELP US BY FOLLOWING THESE INSTRUCTIONS')
    print('.'*20)
    for a, b in enumerate(speclist, 1):
        print("{}. {}".format(a, b))
    i = int(input('Choose a species to explore :) (1-7): '))
    page = requests.get(refs[i-1])
    soup2 = BeautifulSoup(page.text, 'lxml')
    species_img_url = soup2.find(class_='banner').find('img')['src']
    species_img_link = 'https://www.biologicaldiversity.org/' + species_img_url
    species_pic = requests.get(species_img_link)
    species_img = Image.open(BytesIO(species_pic.content))
    species_img.show()
    speciesinfo = [paragraph.text for paragraph in soup2.find(class_= 'col cbd_content_main').find_all('p')]
    print(speclist[i-1])
    for info in speciesinfo:
        if len(info) > 5:
            print(info)
            print("-"*20)
        else:
            pass
    ii = input('Would you like a list of {} that you could help to save? (yes/no) '.format(speclist[i-1]))
    if ii == True:
        species_img.close()
        creeature_page = soup2.find(class_='col-md-4 cbd_content_sidebar').find_all('a')
        creature_links = ['https://www.biologicaldiversity.org/species/' + speclist[i-1].lower() + '/' + creature['href'] for creature in creeature_page if len(creature.text) > 2]
        creature_list = [creature.text for creature in creeature_page if len(creature.text) > 2]
        for a, b in enumerate(creature_list, 1):
            print('{}. {}'.format(a, b.title()))
        print('Choose one to learn more (1-{}): '.format(len(creature_list)))
        iii = int(input(''))
        creature_site = requests.get(creature_links[iii-1])
        creature_soup = BeautifulSoup(creature_site.text, 'lxml')
        creature_summary = creature_soup.find(class_='col-md-6 cbd_content_left').find_all('p')
        creature_img_url = creature_soup.find(class_='banner').find('img')['src']
        creature_img_link = 'https://www.biologicaldiversity.org/' + creature_img_url
        r = requests.get(creature_img_link)
        species_img = Image.open(BytesIO(r.content))
        species_img.show(title='creature_list[iii-1]')
        print('-'*20)
        print('Here\'s a pic of the {}'.format(creature_list[iii-1]))
        print('-'*20)

        for sec in creature_summary:
            print(sec.text)
            print('-'*20)
        print('The {} needs your help!  Click this link to donate: '.format(creature_list[iii-1]))
        print(donatelink)
        
userprogram()
 







