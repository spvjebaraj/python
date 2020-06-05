import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hacker_news_list):
    return sorted(hacker_news_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hacker_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if (points > 99):
                hacker_news.append(
                    {'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hacker_news)


pprint.pprint(create_custom_hacker_news(mega_links, mega_subtext))
# HTNL output - news.html
# print(soup)
