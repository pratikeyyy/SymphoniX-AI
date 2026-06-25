from models.musicgen_provider import MusicGenProvider
from services.prompt_service import PromptService


class MusicService:

    def __init__(self):

        self.provider = MusicGenProvider()

    def generate_music(
        self,
        prompt,
        genre,
        mood,
        duration,
    ):

        final_prompt = PromptService.build(
            prompt,
            genre,
            mood,
        )

        return self.provider.generate(
            final_prompt,
            duration,
        )