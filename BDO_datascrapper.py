#imports

import urllib
from bs4 import BeautifulSoup

target_file = "data.txt"
t = open(target_file,'w')

#Connect to URL
url_base = "https://www.bdo.com.ph/properties-for-sale/real-estate?field_property_is_sale_only_value=All&field_real_estate_area_tid=All&body_value=enter%20search%20term%20here...&title=&field_property_price_value[min]=&field_property_price_value[max]=&field_price_start_value[min]=&field_price_start_value[max]=&field_real_estate_category_tid=All&sort_by=Select&sort_order=Option&prop_type=All&price_range=&custom_sort_dd=Select%20Option&page="
url_end = 41

nice_txt = ''
full_list = []

#parse html
for i in range(url_end):
    url = url_base + str(i)
    response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)


    #Create a list of all data
    for line in soup.find_all('td'):
        if "<img" in line:
            full_list.append("IMAGE")
        else:
            full_list.append(line.get_text(strip=True))

counter = 0
for item in full_list:
    counter = counter + 1
    if counter % 6 == 0:
        nice_txt = nice_txt + item + "\n"
    else:
        nice_txt = nice_txt + item + "\t"

#save data to file.
file = open("BDO-Properties.txt", "w")

file.write(nice_txt.encode('utf-8'))

file.close()
