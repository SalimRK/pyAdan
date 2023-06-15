import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get("https://almaaref.org.lb/")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

date_class = "fw-bold"
emsak_class = "card mx-auto bg-warning text-light mb-1"
fajer_class = "card mx-auto bg-success text-light mb-1"
shorok_calss = "card mx-auto bg-info text-light mb-1"
dohor_class = "card mx-auto bg-primary text-light mb-1"
aser_class = "card mx-auto bg-danger text-light mb-1"

def get_data(html_class):
    # Find the element with the specific class containing the date information
    data_element = soup.find(class_=html_class)  # Replace "your-class" with the appropriate class value
    # Extract the date text
    data_text = data_element.get_text(strip=True)
    return data_text


date_arb = f" مواقيــت الصـــلاة ليوم {get_data(date_class)} حسب توقيت مدينة بيروت "
emsak_arb = "الإمساك"
fajer_arb =  "الفجر"
shorok_arb = "الشروق"
dohor_arb = "الظهر"
aser_arb = "العصر"