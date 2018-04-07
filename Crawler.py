from urllib import request
from urllib import error
from bs4 import BeautifulSoup
import sys

class Crawler(object):
    def __init__(self):
        pass

    def crawl(self, url="http://www.google.com", printout=True):
        req = request.Request(url)
        res = set()
        try:
            response = request.urlopen(req)
            html = response.read()
            soup = BeautifulSoup(html, 'lxml')
            for a in soup.find_all('a'):
                link = a['href']
                res.add(link)
            if (printout):
                for link in res:
                    print(link)
            return res
        except error.URLError as e:
            print(e.reason)

def main():
    cl = Crawler()
    if len(sys.argv) > 1:
        return cl.crawl(sys.argv[1])
    else:
        return cl.crawl()

if __name__ == "__main__":
    main()
