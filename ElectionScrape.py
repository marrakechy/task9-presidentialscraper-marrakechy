import re
import requests

def getTagContent(tag):
	contentRE = re.compile(r">([\S\n\t ]*?)<")
	return contentRE.findall(tag)[0].strip()

def getTotals():

	#useful Regular Expressions:
	tableRE = re.compile(r"<tbody[\S\n\t ]*?</tbody>") # Get the tables
	rowsRE = re.compile(r"<tr[\S\n\t ]*?</tr>") # Get the rows
	dataRE = re.compile(r"<td[\S\n\t ]*?</td>")  # get Table Data
	linkRE = re.compile(r"<a[\S\n\t ]*?</a>")  # get Link Data
	strongRE = re.compile(r"<strong>([\S\n\t ]*?)</strong>")  # get Strong Data  (Years)
	rowSpanRE = re.compile(r"rowspan=\"(\d+)")

	r = requests.get("https://www.britannica.com/topic/electoral-college/U-S-election-results")

	txt = r.text
	#print(txt)
	tables = tableRE.findall(txt)
	t = tables[0]
	#t = tables[0]  # only one table on this page
	rows = rowsRE.findall(t)
	#print(len(rows))
	year = 0
	for r in rows:
		data = dataRE.findall(r)
		if "has-rs" in r: # start of a year
			# first link is the year.
			yeardata =  strongRE.findall(data[0])[0]
			links = linkRE.findall(yeardata)
			#print("Links:", links)
			if len(links) == 0:   #2020 is not in a link :(
				year = 2020
			else:
				year = int(getTagContent(links[0]))

			# first row has year, so candidate name = 1; ev = 3, pop = 4
			candLinks = linkRE.findall(data[1])
			if len(candLinks) == 0:
				candName = getTagContent(data[1])
			else:
				linkCand = linkRE.findall(data[1])
				candName = getTagContent(linkCand[0])
			ev = getTagContent(data[3])
			pop = getTagContent(data[4])
			if pop != "" and ev != "":
				print(year, candName, ev, pop)
		else:
			# other rows don't have year, so candidate name = 0; ev = 2, pop = 3
			if year> 0:
				# print(data)
				candLinks = linkRE.findall(data[0])
				if len(candLinks) == 0:
					candName = getTagContent(data[0])
				else:
					linkCand = linkRE.findall(data[0])
					candName = getTagContent(linkCand[0])
				ev = getTagContent(data[2])
				pop = getTagContent(data[3])
				if pop != "" and ev != "":
					print(year, candName, ev, pop)

getTotals()