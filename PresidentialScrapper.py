# def getPresData(year):
# 	topic = str(year) +"_United_States_presidential_election"
# 	r = requests.get("https://www.presidency.ucsb.edu/statistics/elections/" +topic)
#
# 	txt = r.text
# 	titleRE = re.compile(r"<title.*?</title>")
# 	titles = titleRE.findall(txt)
#
# 	for t in titles:
# 		print(t)
#
#
# 	#print(txt)
#
# def years():
# 	year = 1824
# 	while year <= 2020:
# 		getPresData(year)
# 		year += 4
#
# years()

import requests
from bs4 import BeautifulSoup

url = "https://www.presidency.ucsb.edu/statistics/elections/2020"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#find all tables
tables = soup.find_all('table')
if not tables:
    print("No tables found!")
    exit()

#find specific table we working with
table = tables[0]

data_rows = table.find_all('tr')[1:]

with open('ElectionScrape.txt', 'w') as file:
    #the header to the file
    file.write("Year,State,Candidate Name,Party,Popular Vote,Electoral Votes\n")

    for row in data_rows:
        columns = row.find_all('td')

        if len(columns) == 11:  #main data rows have 11 columns
            state = columns[0].text.strip()

            if 'CD' in state or 'STATE' in state or 'TOTAL VOTES' in state:
                continue
            dem_name = columns[1].text.strip()
            dem_votes = columns[2].text.strip()
            dem_ev = columns[3].text.strip()

            rep_name = columns[4].text.strip()
            rep_votes = columns[5].text.strip()
            rep_ev = columns[6].text.strip()

            file.write(f"2020, {state} , {dem_name} , Democratic , {dem_votes} , {dem_ev} \n")
            file.write(f"2020, {state} , {rep_name} , Republican , {rep_votes} , {rep_ev} \n")
