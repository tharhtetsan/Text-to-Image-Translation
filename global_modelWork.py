import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

class global_modelWork:
    


    def __init__(self):
        self.access_tokens = "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"
        self.model_id = "CompVis/stable-diffusion-v1-4"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, use_auth_token=self.access_tokens, revision="fp16", torch_dtype=torch.float16)
        self.pipe.to(self.device)
        self.write_path = "static/result_images"

    def generate_imgs(self,prompt, num_imgs):
        for i in range(num_imgs):
            # モデルにpromptを入力し画像生成
            with autocast("cuda"):
                image = self.pipe(prompt, guidance_scale=7.5)["sample"][0] 
            # 保存
            image.save(f"{self.write_path}/test_{i:04}.png")

        
 