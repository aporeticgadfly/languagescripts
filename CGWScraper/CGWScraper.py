import requests
from bs4 import BeautifulSoup
import csv

# URL of the CGW page containing example sentences
base_url = 'https://resources.allsetlearning.com/chinese/grammar/'
add_on = '_grammar_points'
page_arr = ['A1', 'A2', 'B1', 'B2']

def has_three_tds(tag):
        return tag.name == "tr" and len(tag.find_all("td")) == 3

with open('CGW_Grammar_Points', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Level", "Grammar Point", "Example", "Pattern"])

    for level in page_arr:
        url = base_url + level + add_on
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract example sentences based on HTML structure
        example_sentences = []

        # Find all <tr> elements with three <td> elements
        matching_trs = soup.find_all(has_three_tds)

        for element in matching_trs:
            columns = element.find_all('td')
            grammar_point = columns[0].get_text().strip()
            example = columns[1].get_text().strip()
            pattern = columns[2].get_text().strip()
            print(level + " " + grammar_point + " " + example + " " + pattern)
            writer.writerow([level, grammar_point, example, pattern])
    f.close()

