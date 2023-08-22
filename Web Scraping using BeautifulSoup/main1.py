# If you want to scrape a website:
# 1. Use the API
# 2. HTML web scraping using some tools like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib
# pip install lxml

from bs4 import BeautifulSoup
with open("home.html", "r") as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, "lxml")
    # print(soup.prettify())

    tags = soup.find("h5") # searches for the first instance only of h5
    # print(tags)

    courses_html_tags = soup.find_all("h5") # finds all the instances of h5
    print(courses_html_tags)

    for course in courses_html_tags:
        print(course.text)