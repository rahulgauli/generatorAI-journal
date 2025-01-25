from gtts import gTTS 


async def collect_speech_from__speech_dict(_speech_dict):
    final_speech = ""
    for key,value in _speech_dict.items():
        final_speech += value["speech"]
    return final_speech


async def ai_audio_generator_(_speech, _news_clip_path):
    final_speech = await collect_speech_from__speech_dict(_speech)
    output_path = f"audio/{_news_clip_path}1234-audio.mp3" 
    tts = gTTS(text=final_speech, lang='en')
    tts.save(output_path)
    return "audio generated thank you"