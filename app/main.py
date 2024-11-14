import os
import asyncio
import requests
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
    return valid_new_response


async def _news_clip_geneartor():
    try:
        clip_content = {}
        response = await get_cnn_news_input("CNN")
    except Exception as e:
        print(e)
        raise 


asyncio.run(_news_clip_geneartor())


