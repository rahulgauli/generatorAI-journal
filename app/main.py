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
            print("Creating folder")
            os.makedirs(folder_path)
        
            with open(f"{folder_path}/cnn_news.json", "w") as json_file:
                json.dump({}, json_file)
                response = await AIJournalist.get_cnn_news_input("CNN", json_file)    
        
        clip_content = {}

        for a_news in response.articles:
            clip_content = {
                "title": a_news['title'],
                "description": a_news['description'],
                "url": a_news['url'],
                "urlToImage": a_news['urlToImage'],
                "publishedAt": a_news['publishedAt'],
                "content": a_news['content']
            }
            print("&&&&&&&&&&&&&&&&&now senidng to AIJournalist&&&&&&&&&&&&&&&&&&&&&")
        async with asyncio.timeout(20):
            summazied_content = await AIJournalist.summarized_content(clip_content)
            after_every_summarized_content_add_a_long_pause = "..."
            cnn_news_audio += after_every_summarized_content_add_a_long_pause
            cnn_news_audio += summazied_content
        return cnn_news_audio
    except Exception as e:
        print(e)
        raise 


if __name__ == "__main__":
    response = asyncio.run(_news_clip_geneartor())
    asyncio.run(ai_audio_generator_(response, folder_path))