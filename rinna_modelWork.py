import torch
from torch import autocast
from diffusers import LMSDiscreteScheduler
from japanese_stable_diffusion import JapaneseStableDiffusionPipeline

class rinna_modelWork:
    


    def __init__(self):
        self.access_tokens = "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"
        self.model_id = "rinna/japanese-stable-diffusion"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
        self.pipe = JapaneseStableDiffusionPipeline.from_pretrained(self.model_id, scheduler=self.scheduler, use_auth_token=self.access_tokens)
        self.pipe = self.pipe.to(self.device)

        self.write_path = "static/result_images"

    def generate_imgs(self,prompt, num_imgs):
        for i in range(num_imgs):
            # モデルにpromptを入力し画像生成
            with autocast("cuda"):
                image = self.pipe(prompt, guidance_scale=7.5)["sample"][0] 
            # 保存
            image.save(f"{self.write_path}/test_{i:04}.png")
