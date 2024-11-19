import torch
from diffusers import MochiPipeline
from diffusers.utils import export_to_video


async def ai_audio_generator_(_speech, _news_clip_path):

    pipe = MochiPipeline.from_pretrained("genmo/mochi-1-preview",
                                         variant="bf16", torch_dtype=torch.bfloat16
                                         )
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_tiling()
    with torch.autocast("cuda", torch.bfloat16, cache_enabled=False):
      frames = pipe(_speech, num_frames=84).frames[0]

    export_to_video(frames, "mochi.mp4", fps=30)
