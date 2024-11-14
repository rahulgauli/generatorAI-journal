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
        print(article_content)
        # return article_content

    @staticmethod
    async def summarized_content(content):
        print("lets summarize the content")
        summarizer = pipeline("summarization", 
                            model="facebook/bart-large-cnn", 
                            framework="pt",
                            device=0
                            )
        print(summarizer)
        content_from_url = await AIJournalist.get_article_content_from_url(content['url'])
        chunks = [content_from_url[i:i+512] for i in range(0, len(content_from_url), 512)]
        print(len(chunks))
        summary = ""
        for achunk in chunks:
            response = (summarizer(achunk, max_length=130, min_length=30, do_sample=False))
            print(response)
            summary += response[0]["summary_text:"]
        return summary