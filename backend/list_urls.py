import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://docs.chaicode.com/youtube/getting-started/"
YOUTUBE_BASE = f"{BASE_URL}/youtube/"

def is_valid_url(url):
    try:
        res = requests.get(url)
        return res.status_code == 200
    except:
        return False
    

def get_urls():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, "html.parser")

    found_urls = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if href.startswith("/youtube/"):
            #normalize to full url
            full_url = urljoin(BASE_URL, href)
            # print(full_url)
            #skip base url or shallow ones like /youtube/
            if full_url == YOUTUBE_BASE:
                continue

            if is_valid_url(full_url):
                found_urls.add(full_url)

    return sorted(found_urls)

# urls_list = get_urls()












































# urls_list = [
#     "https://docs.chaicode.com/youtube/getting-started/",
#     "https://docs.chaicode.com/youtube/chai-aur-html/welcome/",
#     "https://docs.chaicode.com/youtube/chai-aur-html/introduction/",
#     "https://docs.chaicode.com/youtube/chai-aur-html/emmit-crash-course/",
#     "https://docs.chaicode.com/youtube/chai-aur-html/html-tags/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/welcome/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/introduction/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/terminology/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/behind-the-scenes/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/branches/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/diff-stash-tags/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/managing-history/",
#     "https://docs.chaicode.com/youtube/chai-aur-git/github/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/welcome/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/introduction/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/hello-world/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/variables-and-constants/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/data-types/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/operators/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/control-flow/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/loops/",
#     "https://docs.chaicode.com/youtube/chai-aur-c/functions/",
#     "https://docs.chaicode.com/youtube/chai-aur-django/welcome/",
#     "https://docs.chaicode.com/youtube/chai-aur-django/getting-started/",
#     "https://docs.chaicode.com/youtube/chai-aur-django/jinja-templates/",
#     "https://docs.chaicode.com/youtube/chai-aur-django/tailwind/",
#     "https://docs.chaicode.com/youtube/chai-aur-django/models/",
#     "https://docs.chaicode.com/youtube/chai-aur-django/relationships-and-forms/",
#     "https://docs.chaicode.com/youtube/chai-aur-sql/welcome/",
#     "https://docs.chaicode.com/youtube/chai-aur-sql/introduction/",
#     "https://docs.chaicode.com/youtube/chai-aur-sql/postgres/",
#     "https://docs.chaicode.com/youtube/chai-aur-sql/normalization/",
#     "https://docs.chaicode.com/youtube/chai-aur-sql/database-design-exercise/",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
# ]