import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
citysoup = BeautifulSoup(page.text, 'html.parser')
My_table = citysoup.find('table',{'class':'wikitable sortable'})
rows = My_table.find_all('tr')
datarows = rows[1:]
citydict = {}
for data in datarows:
    info = data.find('a')["href"]
    link = 'https://www.wikipedia.org/' + info
    city = data.find('a').text
    #print(city)
    #print(link)
    citydict[city] = link

# function to retrieve user input, get page from wikipedia, and run for loop containing paragraphs from wiki page
def citysummary():
    #ask user for a city and format it (title) to match our dict keys
    userchoice = input('What U.S city would you like to learn about today? ')
    citychoice = userchoice.title()
    url = citydict[citychoice]
    #user input becomes a response for BS4
    response = requests.get(url)
    page_summary = BeautifulSoup(response.text, 'lxml')
    #parse data for wikipedia paragraph tags, then display them as text using for loop.
    summary = page_summary.find(class_='mw-parser-output').find_all('p')
    print('Here\'s a summary of your city')
    print('-------------------')
    #have to skip first <p> tag using '[1]', it's blank on wikipedia
    print(summary[1].text)
    print('There are ' + str(len(summary) - 1) + ' additional paragraphs of info.')
    x = len(summary) - 1
    #for loop ask user if she wants more info, if 'yes' display another <p> tag text
    for summy in summary[2:len(summary)]:

        answer = input('would you like more info? yes/no ')
        if answer.upper() == 'YES':
            print('Here is more for you')
            print('-------------------')
            print(summy.text)
            x -= 1
            print('There are ' + str(x) + ' additional paragraphs of info')
        elif answer.upper() != 'YES':
            print('.........')
            print('Goodbye! have fun reading!')
            print('All info scraped from Wikipedia using requests and BeautifulSoup4 :)')
            print('-from jyron')
            break 
try:
    citysummary()
except KeyError:
    print('I don\'t have info on that city.  Are you sure its spelled correctly?')       

                    
    






    





