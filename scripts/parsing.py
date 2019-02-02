import requests
import bs4
from fake_useragent import UserAgent


def get_rhymes(word):
    """
    :param word: str
    :return rhymes from https://rifme.net: list
    """
    site = requests.get('https://rifme.net/r/' + word, headers={'User-Agent': UserAgent().chrome})

    bs = bs4.BeautifulSoup(site.text, "html.parser")
    rhymes = bs.select('.rifmypodryad')
    rhymes = rhymes[0].find_all('li')
    return [rhyme.get('data-w') for rhyme in rhymes if rhyme.get('data-w')]

