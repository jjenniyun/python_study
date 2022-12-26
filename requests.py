# https://replit.com/my계정/WideLovelyTrapezoids#requests.py
# ---------------------------------------------------------
from requests import get
# get: 하나의 url를 가져오게 함
# 200코드 # 변형
websites = [
  "google.com", "https://httpstat.us/502", "https://httpstat.us/404",
  "https://httpstat.us/300", "https://httpstat.us/200",
  "https://httpstat.us/101"
]
# "https://httpstat.us/xxx is service for generating HTTP codes"

results = {}

# url formatting
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website).status_code
  # print(response.status_code) # response[200]: 성공적으로 응답함
  if response >= 500:
    results[website] = "5xx/ server error"
  elif response >= 400:
    results[website] = "4xx/client error"
  elif response >= 300:
    results[website] = "3xx/redirection"
  elif response >= 200:
    results[website] = "2xx/successful"
    # print(f"{website} is OK")
  elif response >= 100:
    results[website] = "1xx/informational response"
  #else:
  #results[website] = "FAILED"
  #print(f"{website} not OK")

print(results)