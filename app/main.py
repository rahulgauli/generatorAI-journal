from functools import lru_cache
import json
import os
import asyncio
import requests

from app.myAIjournalist import AIJournalist
from .schema import validated_locations, NewsSettings, CNNNewsResponse
from moviepy.video.io.VideoFileClip import VideoFileClip


async def extract_metadata(video: VideoFileClip):
    print("Extracting metadata")
    print({
        "duration": video.duration,
        "fps": video.fps,
        "size": video.size
    })


async def create_short_clips(video, metadata):
    pass


async def get_cnn_news_input(news_channel):
    settings = NewsSettings()
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={settings.cnn}"
    resposne = requests.get(url)
    valid_new_response = CNNNewsResponse(**resposne.json())
    with open("cnn_news.json", "w") as f:
        f.write(resposne.text)
        f.close()
    return valid_new_response


async def _news_clip_geneartor():
    try:
        clip_content = {}
        with open("cnn_news.json", "r") as f:
            clip_content = f.read()
        json_data = json.loads(clip_content)
        json_clip_content = CNNNewsResponse(**json_data)
        for a_news in json_clip_content.articles:
            clip_content = {
                "description": a_news['description'],
                "url": a_news['url'],
                "urlToImage": a_news['urlToImage'],
                "publishedAt": a_news['publishedAt'],
                "content": a_news['content']
            }
            print(clip_content)
            print("&&&&&&&&&&&&&&&&&now senidng to AIJournalist")
            summazied_content = await AIJournalist.summarized_content(clip_content)
            print(summazied_content)
    except Exception as e:
        print(e)
        raise 


asyncio.run(_news_clip_geneartor())


