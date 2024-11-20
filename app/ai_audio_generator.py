# import torch
# from diffusers import MochiPipeline
# from diffusers.utils import export_to_video
# # from melo.api import TTS


# speed = 1.0


# async def ai_audio_generator_(_speech, _news_clip_path):
#     device = 'auto'
#     model = TTS(language='EN', device=device)
#     speaker_ids = model.hps.data.spk2id
#     output_path = 'en-us.wav'
#     model.tts_to_file(_speech, speaker_ids['EN-US'], output_path, speed=speed)
#     return "audio generated thank you"


    # print(output)

    # pipe = MochiPipeline.from_pretrained("genmo/mochi-1-preview", torch_dtype=torch.bfloat16
    #                                      )
    # pipe.enable_model_cpu_offload()
    # pipe.enable_vae_tiling()
    # frames = pipe("guitarist in nature enjoying the natural green view", 
    #               num_inference_steps=28, guidance_scale=3.5).frames[0]

    # export_to_video(frames, "mochi.mp4")

# import asyncio

# if __name__ == "__main__":
#     response = asyncio.run(ai_audio_generator_("response", "folder_path"))
#     #print(response)