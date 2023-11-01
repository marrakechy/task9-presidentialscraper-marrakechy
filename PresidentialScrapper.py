import re
import requests
from bs4 import BeautifulSoup

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



url = "https://www.presidency.ucsb.edu/statistics/elections/2020"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
t = soup.find_all ('table')[0]
rows = t.find_all('tr')
# for table in t:
#     rows = table.find('tr')
for row in rows:
    columns = row.find_all('td')
    for column in columns:
        print(column.text)



# <table>
# <th> (<td> </td>) </th>
# <tr< (<tr> </tr>) </tr>


# st = BeautifulSoup(t[0], 'html')
# tables = st.find_all('tr')
# print(tables)


