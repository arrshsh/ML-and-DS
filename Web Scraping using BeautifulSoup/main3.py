from bs4 import BeautifulSoup
import requests

# Response 200 is a conventional number in web, meaning the request is done successfully
# The code below gives just the response
# html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
# print(html_text)

# To get the actual text, we write the following:
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
# print(html_text)

soup = BeautifulSoup(html_text, "lxml")
# jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
# print(jobs)

# This returns all the instances of li. But for the sake of project, it is good to work with one element and then go on to all elements.
# job = soup.find("li", class_ = "clearfix job-bx wht-shd-bx")
# company_name = job.find("h3", class_ = "joblist-comp-name").text
# print(company_name)

# We see many white spcaes. To replace them, write the following code instead:
job = soup.find("li", class_ = "clearfix job-bx wht-shd-bx")
company_name = job.find("h3", class_ = "joblist-comp-name").text.replace(" ", "")
skills = job.find("span", class_ = "srp-skills").text.replace(" ", "")
# print(company_name)
# print(skills)

# print(f"""
# Company Name : {company_name}
# Required Skills : {skills}
#       """)

# published_date = job.find("span", class_ = "sim-posted")
# print(published_date)

# We see a "span" tag in the "span". Hence, write the following code:
published_date = job.find("span", class_ = "sim-posted").span.text
print(published_date)