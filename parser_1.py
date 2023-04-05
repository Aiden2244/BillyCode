# import statements for using other libraries

import requests # to make a request to a website
from bs4 import BeautifulSoup # to parse the html content
import pandas as pd # to import structures that store and can manipulate data

# define the website we want to scrape
url = "https://www.history.com/topics/holidays/passover"
domain = "https://www.history.com"

# make a request to the website
response = requests.get(url)
html_content = response.content # stores the html content of the website

# print(html_content) # to see all of the html content

# parse the html content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# find all the links on the website
links = soup.find_all("a") # a is the html tag for links

# store the links in a list
child_links = []

# loop through the links and store only the links that are relevant to the website
for current_link in links:
    # in English: "if object called 'current_link' has an html link associated with it,
    # and if the link starts with a forward slash (i.e. it is from the same website),
    # add the main url to the link and add it to the list of child links"
    if current_link.has_attr("href") and current_link["href"].startswith("/"):
        child_links.append(domain + current_link["href"])

# create a dataframe from the list of child links
child_links_df = pd.DataFrame(child_links, columns=["links"])

# save the dataframe as a csv (comma separated value) file
child_links_df.to_csv("child_links.csv", index=False)
        



