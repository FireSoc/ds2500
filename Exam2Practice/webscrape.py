import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all links
for link in soup.find_all("a"):
    print(link.get("href"))  # Prints all URLs

table = soup.find("table")
print(table)
if table:
    rows = table.find_all("tr")

    for row in rows:
        columns = row.find_all("td")
        data = [col.text for col in columns]
        print(data)

# .text gets text inside a tag
# .get extracts values like links
# .find gives first time of given tag
# find_all gives all matching tags
# can find by id and class also
# .select("css-selector")
