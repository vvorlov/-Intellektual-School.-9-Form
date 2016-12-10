from bs4 import BeautifulSoup
import requests

# parse football matches schedule
url = "http://terrikon.com/football/russia/championship/"

# get html code
html_doc = requests.get(url).text

# prepare object for parsing
soup = BeautifulSoup(html_doc, "lxml")  # html5lib

# get all rows with correct class
table = soup.find('table', {'class': 'gameresult'}).findAll('tr')

# get correct info
for item in table:
    teams = item.findAll('td', {'class': 'team'})
    for t in teams:
        print t.text
    date = item.find('td', {'class': 'date'}).text
    print date
