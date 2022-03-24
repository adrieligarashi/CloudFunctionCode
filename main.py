import requests
from bs4 import BeautifulSoup

import json
import datetime

from google.cloud import storage


BUCKET_NAME = "le-wagon-data"  # 🚨 replace with your bucket name


def storage_upload(request):
    """
    cloud function entry point
    """

    pass  # YOUR CODE HERE

    # all printed output will be visible in the Cloud Function logs
    print("it works!")

    # the returned json response
    return {"response": "the Cloud Function json response, if any"}


def top_3_from_hackernews():
    """
    return top 3 news from hackernews
    """

    url = "https://news.ycombinator.com/"
    resposta = requests.get(url)
    sopa = BeautifulSoup(resposta.content, "html.parser")

    titulo = []
    titulos_html = sopa.find_all('a', class_='titlelink')

    for tit in titulos_html:
        title = tit.string
        titulo.append(title)

    return titulo[0:3]


if __name__ == '__main__':

    res = top_3_from_hackernews()
    print(res)
