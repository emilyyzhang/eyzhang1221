import time
from selenium import webdriver
chromedriver_path = "/Users/emilyzhang/Downloads/chromedriver" # path to the downloaded chromedriver
from bs4 import BeautifulSoup


def WebScraper():
    '''
    scrapes Conference Proceedings and workshops papers from
    https://www.usenix.org/publications/proceedings
    '''
    
    baseurl = "https://www.usenix.org/publications/proceedings?page="
    driver2 = webdriver.Chrome(chromedriver_path)

    for i in range(1, 10):
        url = baseurl + str(i)
        driver2.get(url)
        page_source = driver2.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        soup.prettify()

        for paper in soup.find_all('tr'):
            try: Class = paper['class']
            except: continue
            if str(Class[0]) != 'even' and str(Class[0]) != 'odd': continue

            print(paper.get_text(' | '))

    driver2.quit()

if __name__ == "__main__":
    WebScraper()
