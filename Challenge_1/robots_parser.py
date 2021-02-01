from bs4 import BeautifulSoup
import requests


def robots_parser():
    url = 'https://mlh-ctf-usaf-01.herokuapp.com/robots.txt'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)


robots_parser()