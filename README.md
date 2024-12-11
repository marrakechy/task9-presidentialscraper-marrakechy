# US Presidential Election Data Scraper

## Project Overview
This project implements a web scraper to collect and aggregate United States presidential election data from 1824 to 2020. The scraper pulls data from either Wikipedia or the UCSB Presidency Project to create a comprehensive dataset of election results.

## Objectives
- Use a scraper to programmatically aggregate data from multiple sources
- Demonstrate the ability to scrape data from real sources
- Experience the quality of structured data in the wild

## Data Sources
The scraper can pull data from either or both of these sources:
- Wikipedia: `https://en.wikipedia.org/wiki/United_States_presidential_election,_YEAR`
- UCSB Presidency Project: `http://www.presidency.ucsb.edu/statistics/elections/YEAR`

## Output Files

### 1. ElectionScrape.txt
Contains the main election data in the following format:

Year, State, Candidate Name, Party, Popular Vote, Electoral Votes


### 2. unpopularElectoralVotes.txt
Contains records of electoral votes awarded by means other than popular vote:

Year, State, Electoral Votes, Candidate

## Major Candidate Criteria
The scraper includes data for "major candidates" defined as those who:
- Participated in the general election as head of ticket
- Received at least one electoral vote in that year

Examples:
- ✓ Strom Thurmond (1948) - Included (won popular and electoral votes, head of Dixiecrat ticket)
- ✗ Ross Perot (1992) - Not included (no electoral votes)
- ✗ Harry Byrd (1960) - Not included (not head of ticket)
- ✗ John Edwards (2004) - Not included (not head of ticket)

## Special Cases Handled
The scraper accounts for several special scenarios:
1. Electors selected by legislature (e.g., 1824)
2. Unpledged Delegates (e.g., 1960)
3. Faithless Electors (e.g., 2004, 2016)
4. Multiple tickets per party (e.g., 1836 Whigs)

## Requirements
- Python 3.x
- BeautifulSoup4
- Requests
- Other dependencies listed in requirements.txt

## Installation

git clone [repository-url]
cd [repository-name]
pip install -r requirements.txt


## Usage
python election_scraper.py


## Project Structure
├── election_scraper.py    
├── ElectionScrape.txt      
├── unpopularElectoralVotes.txt  
├── requirements.txt        
└── excuse_document.txt     

## Known Limitations
Please refer to excuse_document.txt for a detailed list of known data gaps and the rationale behind why certain data points could not be scraped.

## Contributing
This is an academic project completed as part of [Course Name]. While it's not open for contributions, you're welcome to fork the repository and adapt it for your own use.

## Author
Brahim El-Marrakechy

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Data sources: Wikipedia and The American Presidency Project (UCSB)
- [DataCentric] for project specifications and guidance
