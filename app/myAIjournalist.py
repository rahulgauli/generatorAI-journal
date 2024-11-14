import requests
import datetime
from bs4 import BeautifulSoup
from transformers import pipeline
from app.schema import CNNNewsResponse, NewsSettings


class AIJournalist:


    @staticmethod
    async def get_cnn_news_input(news_channel):
        todays_date = datetime.datetime.now().date()
        settings = NewsSettings()
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={settings.cnn}"
        resposne = requests.get(url)
        valid_new_response = CNNNewsResponse(**resposne.json())
        with open(f"{todays_date}/cnn_news.json", "w") as f:
            f.write(resposne.text)
            f.close()
        return valid_new_response


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
        return response