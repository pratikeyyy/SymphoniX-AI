"""
MusicGen Provider
SymphoniX AI
"""

from pathlib import Path
import time
import scipy.io.wavfile as wavfile
import torch

from transformers import (
    AutoProcessor,
    MusicgenForConditionalGeneration,
)


class MusicGenProvider:

    def __init__(self):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        print("=" * 60)
        print("Loading MusicGen...")
        print(f"Device : {self.device}")
        print("=" * 60)

        self.processor = AutoProcessor.from_pretrained(
            "facebook/musicgen-small"
        )

        self.model = MusicgenForConditionalGeneration.from_pretrained(
            "facebook/musicgen-small"
        ).to(self.device)

        self.sample_rate = (
            self.model.config.audio_encoder.sampling_rate
        )

        Path("generated").mkdir(exist_ok=True)

        print("MusicGen Loaded Successfully")

    def generate(
        self,
        prompt: str,
        duration: int = 10,
    ):

        inputs = self.processor(
            text=[prompt],
            padding=True,
            return_tensors="pt",
        )

        inputs = {
            k: v.to(self.device)
            for k, v in inputs.items()
        }

        start = time.time()

        audio = self.model.generate(
            **inputs,
            max_new_tokens=duration * 50,
        )

        filename = (
            Path("generated")
            / f"music_{int(time.time())}.wav"
        )

        wavfile.write(
            filename,
            self.sample_rate,
            audio[0, 0].cpu().numpy(),
        )

        elapsed = round(time.time() - start, 2)

        return str(filename), elapsed