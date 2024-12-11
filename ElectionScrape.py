import requests
from bs4 import BeautifulSoup
import csv
import re
from typing import Dict, List, Tuple, Set
import logging
from datetime import datetime


logging.basicConfig(
	filename=f'scraper_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
	level=logging.INFO,
	format='%(asctime)s - %(levelname)s - %(message)s'
)


class ElectionScraper:
	def __init__(self):
		self.session = requests.Session()
		#mimic the browser
		self.session.headers.update({
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
		})
		self.election_data = []
		self.unpopular_electoral_votes = []

	def fetch_page(self, url: str) -> BeautifulSoup:
		try:
			response = self.session.get(url)
			response.raise_for_status()
			return BeautifulSoup(response.text, 'html.parser')
		except Exception as e:
			logging.error(f"error fetching {url}: {str(e)}")
			return None

	def process_wikipedia_page(self, year: int) -> None:
		"""Process a election page for a given year."""
		url = f"https://en.wikipedia.org/wiki/United_States_presidential_election,_{year}"
		soup = self.fetch_page(url)
		if not soup:
			return

		try:

			results_table = soup.find('table', class_='wikitable')
			if not results_table:
				logging.warning(f"no results table found for {year}")
				return

			state_results = self._extract_state_results(results_table, year)

			major_candidates = self._identify_major_candidates(results_table, year)

			self._process_state_results(state_results, major_candidates, year)

		except Exception as e:
			logging.error(f"Error processing {year}: {str(e)}")

	def _extract_state_results(self, table: BeautifulSoup, year: int) -> Dict:
		state_results = {}
		for row in table.find_all('tr')[1:]:  # Skip header row
			cols = row.find_all(['td', 'th'])
			if len(cols) < 4:  # Skip rows without enough columns
				continue

			state_name = cols[0].get_text().strip()
			if not self._is_valid_state(state_name):
				continue

			try:
				votes = {
					'electoral_votes': int(cols[-1].get_text().strip()),
					'popular_votes': self._extract_popular_votes(cols)
				}
				state_results[state_name] = votes
			except ValueError:
				continue

		return state_results

	def _identify_major_candidates(self, table: BeautifulSoup, year: int) -> Set[str]:

		major_candidates = set()
		# Implementation would identify candidates who received electoral votes
		# and were head of ticket
		return major_candidates

	def _process_state_results(self, state_results: Dict, major_candidates: Set[str], year: int) -> None:

		for state, results in state_results.items():
			if self._is_unpopular_electoral_vote(results, year, state):
				self.unpopular_electoral_votes.append({
					'Year': year,
					'State': state,
					'Electoral_Votes': results['electoral_votes'],
					'Candidate': results.get('winner', 'Unknown')
				})
			else:
				self._add_to_main_results(year, state, results, major_candidates)

	def save_results(self):

		with open('ElectionScrape.txt', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(['Year', 'State', 'Candidate Name', 'Party', 'Popular Vote', 'Electoral Votes'])
			writer.writerows(self.election_data)

		# Save unpopular electoral votes
		with open('unpopularElectoralVotes.txt', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(['Year', 'State', 'Electoral Votes', 'Candidate'])
			writer.writerows([
				[row['Year'], row['State'], row['Electoral_Votes'], row['Candidate']]
				for row in self.unpopular_electoral_votes
			])

	def run(self):
		for year in range(1824, 2021, 4):
			logging.info(f"Processing year {year}")
			self.process_wikipedia_page(year)

			if not self.election_data:
				self.process_presidency_page(year)
		self.save_results()


	def _is_valid_state(self, state: str) -> bool:
		"""check if a string represents a valid US state."""
		pass

	def _extract_popular_votes(self, cols: List) -> Dict:
		"""extract popular vote counts from table columns."""
		pass

	def _is_unpopular_electoral_vote(self, results: Dict, year: int, state: str) -> bool:
		"""determine if electoral votes were awarded by means other than popular vote."""
		pass

	def _add_to_main_results(self, year: int, state: str, results: Dict, major_candidates: Set[str]):
		"""add valid results to the main election data list."""
		pass


if __name__ == "__main__":
	scraper = ElectionScraper()
	scraper.run()


