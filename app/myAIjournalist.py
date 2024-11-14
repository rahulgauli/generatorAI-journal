#character
#settings 
#3d news channel settings 
#news channel settings that looks like a big national TV channel settings

from transformers import pipeline
import requests


class AIJournalist:

    @staticmethod
    async def get_article_content_from_url(url):
        article = requests.get(url)
        article_content = article.text
        return article_content

    @staticmethod
    async def summarized_content(content):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        content_from_url = await AIJournalist.get_article_content_from_url(content['url'])
        response = (summarizer(content_from_url, max_length=130, min_length=30, do_sample=False))
        return response[0]['summary_text']
