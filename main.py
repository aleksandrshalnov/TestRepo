import requests
from bs4 import BeautifulSoup
import json

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

req = requests.get("https://selectel.ru/blog/courses/", headers)
req_response_text = req.text

soup = BeautifulSoup(req_response_text, features="html.parser")
allCourses = soup.findAll('li', class_='info-page_material-item')
filtered_courses = []

for course in allCourses:
    t = course.find('h3', class_ ='course-card_title')
    if t is not None:
        filtered_courses.append(t.get_text(strip=True))


print(filtered_courses)
    # with open("_html_req.txt", "w", encoding="utf-8") as f:
    #     f.write(req_response_text)

        # if __name__ == '__main__':
        #
        #     print_hi('PyCharm')
