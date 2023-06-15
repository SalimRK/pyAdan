import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get("https://almaaref.org.lb/")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

date_class = "fw-bold"
imsak_class = "card mx-auto bg-warning text-light mb-1"
fajr_class = "card mx-auto bg-success text-light mb-1"
shorok_calss = "card mx-auto bg-info text-light mb-1"
dohor_class = "card mx-auto bg-primary text-light mb-1"
aser_class = "card mx-auto bg-danger text-light mb-1"
mogreb_class = "card mx-auto bg-secondary text-light mb-1"
esha_class = "card mx-auto bg-dark text-light mb-1"
mid_night_class = "card mx-auto bg-dark text-light mb-1"


def get_data(html_class):
    # Find the element with the specific class containing the date information
    data_element = soup.find(class_=html_class)  # Replace "your-class" with the appropriate class value
    # Extract the date text
    data_text = data_element.get_text(strip=True)
    return data_text


date_arb = f" مواقيــت الصـــلاة ليوم {get_data(date_class)} حسب توقيت مدينة بيروت "
imsak_arb = "الإمساك"
fajr_arb = "الفجر"
shorok_arb = "الشروق"
dohor_arb = "الظهر"
aser_arb = "العصر"
mogreb_arb = "المغرب"
esha_arb = "العشاء"
mid_night_arb = "منتصف الليل"

imsak_time = get_data(imsak_class)
fajr_time = get_data(fajr_class)
shorok_time = get_data(shorok_calss)
dohor_time = get_data(dohor_class)
aser_time = get_data(aser_class)
mogreb_time = get_data(mogreb_class)
esha_time = get_data(esha_class)
mid_night_time = get_data(mid_night_class)

if __name__ == '__main__':
    print(date_arb)
    print(imsak_arb + " : " + imsak_time)
    print(fajr_arb + " : " + fajr_time)
    print(shorok_arb + " : " + shorok_time)
    print(dohor_arb + " : " + dohor_time)
    print(aser_arb + " : " + aser_time)
    print(mogreb_arb + " : " + mogreb_time)
    print(esha_arb + " : " + esha_time)
    print(mid_night_arb + " : " + mid_night_time)
