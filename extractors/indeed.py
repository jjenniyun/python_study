from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
#from extractors.wwr import extract_wwr_jobs

#jobs= extract_wwr_jobs("python")
#print(jobs)
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

def get_page_count(keyword):
  url = "https://kr.indeed.com/jobs?q="
  end_url = "&limit=50"
  browser.get(f"{url}{keyword}{end_url}")

  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", attrs={"aria-label":"pagination"})
  pages = pagination.select("div a")
  # find_all("div", recursive=False)
  count = len(pages)+1
  for page in pages:
    if page['aria-label'] == "Previous Page":
      count -= 1
    if page['aria-label'] == "Next Page":
      count -= 1
  if count >= 5:
    return 5
  else:
    return count

#print(get_page_count("python"))
#print(get_page_count("ruby"))
#print(get_page_count("nextjs"))
#print(get_page_count("django"))
#print(get_page_count("nestjs"))
#print(get_page_count("java"))
#print(get_page_count("react"))
#print(get_page_count("c#"))

def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  print("Found",pages,"pages")
  result = []
  for page in range(pages):
    url = "https://kr.indeed.com/jobs?"
    final_url = f"{url}q={keyword}&start={page*10}"
    print("Requesting", final_url)
    #end_url = "&limit=50"
    browser.get(final_url)
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = (soup.find("ul", class_="jobsearch-ResultsList"))
    jobs = job_list.find_all('li', recursive=False)
    # ul 바로 밑 li만 찾아낼 것
    #print(len(jobs))
    
    for job in jobs:
      # find는 찾은 element를 주거나 None을 준다
      zone = job.find("div",class_="mosaic-zone")
      # job li에서 job을 추출함
      if zone == None: # 무언가 없을 때 사용하는 자료형
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div",class_="companyLocation")
        job_data = {
          'link': f"https://kr.indeed.com{link}",
          'company':company.string.replace(","," "),
          'location':location.string.replace(","," "),
          'position':title.replace(","," ")
        }
    for each in job_data:
      if job_data[each] != None:
        job_data[each] = job_data[each].replace(","," ")
        result.append(job_data)
  return result
  
#jobs = extract_indeed_jobs("python")
#print(jobs)

#print(len(jobs))
#print(get_page_count("django"),get_page_count("nestjs"), get_page_count("c#"))