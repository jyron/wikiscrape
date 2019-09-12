import re
import csv
import requests
from bs4 import BeautifulSoup

# get packages first--> pip install requests beautifulsoup4
# then run file in terminal --> python3 stateofunion.py
# this script will create a csv file with every state of the union address since George Washington in 1790

url = 'https://en.wikisource.org/wiki/Portal:State_of_the_Union_Speeches_by_United_States_Presidents'
pages = requests.get(url)
soup = BeautifulSoup(pages.text, 'lxml')
listoflinks = soup.find('div', attrs={"class": "mw-parser-output"})
links = listoflinks.find_all(href=re.compile('Address'))
union_links = ['https://en.wikisource.org' + link['href'] for link in links]
csv_list = []

def text_getter(path,csv_list):
    try:
        page = requests.get(path)
        warmsoup = BeautifulSoup(page.text, 'lxml')
        # header div contains the president and title
        page_header = warmsoup.find('div', attrs={"class": "gen_header_title"})
        # p divs contain speech transcripts
        state_of_union = warmsoup.find_all('p')
        # these vars define columns of csv
        title = page_header.find('span').text
        president = page_header.find('span', attrs={"class": "fn"}).text
        speech_text = [par.text.rstrip() for par in state_of_union[:len(state_of_union)-1]]
        year = re.search(r'\d\d\d\d', page_header.text).group(0)
        csv_list.append([president, year, title, speech_text])
    except:
        pass
    

for path in union_links:
    text_getter(path, csv_list)
        
with open('state_ofthe_union_texts.csv', mode='w') as speech_data:
    head_row = ['President', 'Year', 'Title', 'Text']
    ewriter = csv.writer(speech_data)
    ewriter.writerow(head_row)
    ewriter.writerows(csv_list)
    


    



    






