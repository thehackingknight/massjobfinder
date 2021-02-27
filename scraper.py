import requests, logging
from bs4 import BeautifulSoup
import html


def soup_fetcha(url):

    res = requests.get(url)
    s = BeautifulSoup(res.text, "html.parser")
    return s


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
        return full_desc

    def careers24(self, url):
        print(url)
        url = f"https://careers24.com{url}"
        soup = soup_fetcha(url)
        full_desc = str(soup.select_one(".c24-vacancy-details-container"))
        #full_desc += str(f'<a href={url} target="_blank" class="btn-outline-success btn btn-sm">Apply on LinkedIn</a>')
        
        #with open('jobs.html', 'w', encoding='utf-8') as jbs:
        #    jbs.write(full_desc)
        #print("Done")
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

        url = f"https://indeed.com/jobs?q={query}"
        soup = soup_fetcha(url)
        job_list = []
        jobs = soup.select(".jobsearch-SerpJobCard.result")

        with open('jobs.html', 'w') as jbs:

            jbs.write(str(jobs))
        for job in jobs:

            title = job.select_one('.title').get_text()
            href = job.select_one('.jobtitle')["href"]
            meta = job.select_one(".summary").get_text()
            meta = meta[0:351]
            job_list.append({"title": title,"meta" : meta, "href": href, "site" : "Indeed", "site_url" : "https://indeed.com"})
        return job_list


    def careers24(self, query):
        query = f"https://www.careers24.com/jobs/kw-{query}/rmt-incl/"
        soup = soup_fetcha(query)
        job_list = []
        jobs = soup.select(".job-card")
        for job in jobs:
    
            title = job.select_one('.job-card-head a').get_text()
            href = job.select_one('.job-card-head a')["href"]
            meta = job.select_one("ul")
            #meta = meta[0:351]
            job_list.append({"title": title,"meta" : meta, "href": href, "site" : "Careers24", "site_url" : "https://careers24.com"})
        #print(job_list) 
        return job_list

    def jobs(self, query):
    
        job_list = self.linkedin(query) + self.indeed(query) + self.careers24(query)
        return  sorted(job_list, key = lambda i:i["title"])

Jobs().careers24('python')