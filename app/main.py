import json
import os
import asyncio
import datetime
from .ai_audio_generator import ai_audio_generator_
from app.myAIjournalist import AIJournalist
from .schema import CNNNewsResponse
# from moviepy.video.io.VideoFileClip import VideoFileClip


today_date = datetime.datetime.now().date()
folder_path = f"dailyAInews/{today_date}"


async def _news_clip_geneartor():
    try:
    
        cnn_news_audio = ""
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            await AIJournalist.get_cnn_news_input("CNN")    
        today_date = datetime.datetime.now().date()
        clip_content = {}
        with open(f"dailyAInews/{today_date}/cnn_news.json", "r") as f:
            clip_content = f.read()
        json_data = json.loads(clip_content)
        json_clip_content = CNNNewsResponse(**json_data)
        for a_news in json_clip_content.articles:
            clip_content = {
                "title": a_news['title'],
                "description": a_news['description'],
                "url": a_news['url'],
                "urlToImage": a_news['urlToImage'],
                "publishedAt": a_news['publishedAt'],
                "content": a_news['content']
            }
            print("&&&&&&&&&&&&&&&&&now senidng to AIJournalist")
            summazied_content = await AIJournalist.summarized_content(clip_content)
            after_every_summarized_content_add_a_long_pause = "............"
            cnn_news_audio += after_every_summarized_content_add_a_long_pause
            cnn_news_audio += summazied_content
        return cnn_news_audio
    except Exception as e:
        print(e)
        raise 


response = asyncio.run(_news_clip_geneartor())
asyncio.run(ai_audio_generator_(response))

