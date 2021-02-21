import requests, json
from bs4 import BeautifulSoup

def soup_fetcha(url):
    
    s = BeautifulSoup(requests.get(url).text, "html.parser")
    return s

def pnet(keyword):
    
    job_list = []
    url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}"
    params = {"ke": "java", "lang": "en"}
    soup = soup_fetcha(url)
    titles = soup.select('.result-card__full-card-link')
    jobs = soup.select('.jobs-search__results-list li')
    for job in jobs:
        title = job.select_one('a').get_text()
        meta = job.select_one('.job-result-card__meta')
        href = job.select_one('a')["href"]
        job_list.append({"title": title, "meta" : meta, "href":href})

    return job_list


