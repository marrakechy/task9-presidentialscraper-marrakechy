# def getPresData(year):
# 	topic = str(year) +"_United_States_presidential_election"
# 	r = requests.get("https://www.presidency.ucsb.edu/statistics/elections/" +topic)

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

def PresData(year):

    #topic = str(year) +"_United_States_presidential_election"
    url = (f"https://www.presidency.ucsb.edu/statistics/elections/{year}" )
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup)


    if year in range(1824, 2016):

        tables = soup.find_all('table')
        if not tables:
            print(f"No tables found for year {year}!")
            return

        table = tables[0]
        data_rows = table.find_all('tr')[1:]

        with open('ElectionScrape.txt', 'a') as file:
            file.write("Year,State,Candidate,Party,Popular Vote,Electoral Votes\n")


            for row in data_rows:
                columns = row.find_all('td')

                if len(columns) < 6 or 'STATE' in columns[0].text:
                    continue

                state = columns[0].text.strip()
                if state == "" or state == "Votes":
                    continue

                votes_1 = columns[2].text.strip()
                party1 = "Candidate name1"
                ev_1 = columns[4].text.strip()

                votes_2 = columns[5].text.strip()
                party2 = "candidate name2"
                ev_2 = columns[7].text.strip()

                file.write(f"{year} , {state} , {party1} , {votes_1} , {ev_1}\n")
                file.write(f"{year} , {state} , {party2} , {votes_2} , {ev_2}\n")

    else:

        tables = soup.find_all('table')
        if not tables:
            print("No tables found!")
            exit()

        #find specific table we working with
        table = tables[0]
        data_rows = table.find_all('tr')[1:]

        #print(data_rows)

        #0 2 4 5
        with open('ElectionScrape.txt', 'a') as file:
            #the header to the file
            file.write("Year,State,Candidate Name,Party,Popular Vote,Electoral Votes\n")

            for row in data_rows:
                columns = row.find_all('td')

                if len(columns) == 11:
                    state = columns[0].text.strip()

                    if 'CD' in state or 'STATE' in state or 'TOTAL VOTES' in state:
                        continue

                    dem_votes = columns[2].text.strip()
                    dem_ev = columns[4].text.strip()

                    rep_votes = columns[5].text.strip()
                    rep_ev = columns[7].text.strip()


                    file.write(f"{year}, {state} , candidate name1  , Democratic , {dem_votes}, {dem_ev}  \n")
                    file.write(f"{year}, {state} , candidate name2  , Republican , {rep_votes}, {rep_ev} \n")

def years():
	year = 1824
	while year <= 2020:
		PresData(year)
		year += 4

years()