import requests, logging
from bs4 import BeautifulSoup
import html

def req(q):
    url = f"https://indeed.com/jobs?q={q}"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    return soup

def soup_fetcha(url):

    s = BeautifulSoup(requests.get(url).text, "html.parser")
    return s

def get_full_desc(url):

    href_soup = soup_fetcha(f"https://indeed.com{url}")
    full_desc = href_soup.select_one("#viewJobSSRRoot")
    return full_desc

class GetFullDesc():

    def __init__(self):
        super().__init__()

    def indeed(self, url):

        href_soup = soup_fetcha(f"https://indeed.com{url}")
        full_desc = href_soup.select_one("#viewJobSSRRoot")
        return full_desc

    def linkedin(self, url):

        soup = soup_fetcha(url)
        full_desc = str(soup.select_one('.description'))
        full_desc += str(f'<a href={url} target="_blank" class="btn-outline-success btn btn-sm">Apply on LinkedIn</a>')
        
        with open('jobs.html', 'w', encoding='utf-8') as jbs:
            jbs.write(full_desc)
        print("Done")
        return full_desc

class Jobs():

    def __init__(self):
        super().__init__()

    def linkedin(self, keyword):
        
        job_list = []
        url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}"
        soup = soup_fetcha(url)
        jobs = soup.select('.jobs-search__results-list li')
        for job in jobs:
            title = job.select_one('a').get_text()
            meta = job.select_one('.job-result-card__meta p').get_text()
            href = job.select_one('a')["href"]
            job_list.append({"title": title, "meta" : meta, "href":href, "site" : "LinkedIn", "site_url" : "https://indeed.com"})

        return job_list

    def indeed(self, query):

        soup = req(query)
        job_list = []
        jobs = soup.select(".jobsearch-SerpJobCard.result")
        for job in jobs:

            title = job.select_one('.title').get_text()
            href = job.select_one('.jobtitle')["href"]
            meta = job.select_one(".summary").get_text()
            meta = meta[0:351]
            job_list.append({"title": title,"meta" : meta, "href": href, "site" : "Indeed", "site_url" : "https://indeed.com"})
        return job_list

    def jobs(self, query):
    
        job_list = self.linkedin(query) + self.indeed(query)
        return  sorted(job_list, key = lambda i:i["title"])

 