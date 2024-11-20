# from fastapi import HTTPException
import requests
import datetime
from bs4 import BeautifulSoup
from transformers import pipeline
from app.schema import CNNNewsResponse, NewsSettings
import serpapi



from functools import lru_cache
import requests

@lru_cache(maxsize=100)
async def fetch_data(url):
    print("fetching data")
    response = requests.get(url)
    if response.status_code == 200:
        valid_new_response = CNNNewsResponse(**response.json())
        return valid_new_response
    else:
        response.raise_for_status()


class AIJournalist:

    async def get_trends():
        url = "https://serpapi.com/search?engine=google_trends_trending_now"
        params = {
        "api_key": "93817e23fea7e075bcca50eee02c9648006be403a00365d65beffe1d00018511",
        "engine": "google_trends_trending_now",
        "geo": "US",
        "hours": "12",
        "hl": "en"
        }

        search = serpapi.search(params)
        search_json = search.as_dict()
        return search_json


    @staticmethod
    async def get_cnn_news_input():
        try:
            settings = NewsSettings()
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={settings.cnn}"
            return await fetch_data(url)
            # valid_new_response = CNNNewsResponse(**response.json())
            # return valid_new_response
        except Exception as e:
            print(e)
            raise
      

    @staticmethod
    async def get_article_content_from_url(url):
        article = requests.get(url)
        soup = BeautifulSoup(article.content, "html.parser")
        article_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        return article_text


    @staticmethod
    async def summarized_content(content):
        print("lets summarize the content")
        summarizer = pipeline("summarization", 
                            model="facebook/bart-large-cnn", 
                            framework="pt",
                            device=0
                            )
            
        content_from_url = await AIJournalist.get_article_content_from_url(content['url'])
        response = summarizer(content_from_url)
        return response[0]['summary_text']