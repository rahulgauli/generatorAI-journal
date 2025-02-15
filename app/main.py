import json
import os
import asyncio
import datetime
from .ai_audio_generator import ai_audio_generator_
from app.myAIjournalist import AIJournalist
from .schema import CNNNewsResponse
# from moviepy.video.io.VideoFileClip import VideoFileClip
from collections import Counter
import re


async def validate_if_trendy_words_in_news(news, trends):
    for word in news:
        if word in trends:
            return True
    return False


async def get_unique_words(strings):
    words = []
    for s in strings:
        tokens = re.findall(r'\b\w+\b', s.lower())
        words.extend(tokens)
    word_counts = Counter(words)
    unique_words = [word for word, count in word_counts.items() if count >= 5]
    if len(unique_words) > 1:
        return unique_words


async def _news_clip_geneartor():
    try:
        trends = []
        cnn_news_audios = {}
        _news = await AIJournalist.get_cnn_news_input()
        _trends = await AIJournalist.get_trends()
        index = 0
        for a_trend in _trends['trending_searches']:    
            try:
                # print(a_trend)
                if a_trend["search_volume"] > 500:
                    trends.append(a_trend["query"])
                trendy_words_for_single_trend_breakdown = await get_unique_words(a_trend["trend_breakdown"])
                if trendy_words_for_single_trend_breakdown:
                    for a_trendy_word in trendy_words_for_single_trend_breakdown:
                        trends.append(a_trendy_word)
                    index += 1
            except KeyError:
                pass
        print(trends)
        article_index=0
        for a_news in _news.articles:
            if a_news["title"] and a_news["description"]:
                words_to_select = a_news['title'].split(" ") + a_news['description'].split(" ")
                match = await validate_if_trendy_words_in_news(words_to_select, trends)
                if match:
                    cnn_news_audios[article_index] = {"speech":a_news["title"] + " " + a_news["description"],
                                                      "hashtags": words_to_select
                                                      }
                    article_index += 1
                    title = a_news['title'].split(" ")
                    description = a_news['description'].split(" ")
                    full_list_of_words = title + description
                    match = await validate_if_trendy_words_in_news(full_list_of_words, trends)
        return cnn_news_audios
    except Exception as e:
        print(e)
        raise 


if __name__ == "__main__":
    response = asyncio.run(_news_clip_geneartor())
    assert len(response) > 0
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    folder_path = f"speech_for_{date}"
    with open(f"speech_for_{date}.json", "w") as f:
        f.write(json.dumps(response))
    asyncio.run(ai_audio_generator_(response, folder_path))