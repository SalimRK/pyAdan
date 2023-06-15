import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get("https://almaaref.org.lb/")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the container that holds the prayer times
container = soup.find("div", class_="card h20 mb-3")

# Extract the prayer times
prayer_times = container.find_all("td")

# Print the prayer times
for prayer in prayer_times:
    print(prayer.get_text(strip=True))
