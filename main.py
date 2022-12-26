from requests import get
# get: 하나의 url를 가져오게 함
# 200코드
websites = [
  "google.com", 
  "airbnb.com", 
  "https://twitter.com", 
  "facebook.com",
  "https://tiktok.com"
]

results = {}

# url formatting
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  # print(response.status_code) # response[200]: 성공적으로 응답함
  if response.status_code == 200:
    results[website] = "OK"
    # print(f"{website} is OK")
  else:
    results[website] = "FAILED"
    #print(f"{website} not OK")
    
print(results)