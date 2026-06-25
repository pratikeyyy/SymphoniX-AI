"""
Prompt Enhancement Service
"""


class PromptService:

    @staticmethod
    def build(
        prompt: str,
        genre: str,
        mood: str,
    ) -> str:

        return (
            f"""
Professional {genre} soundtrack.

Mood:
{mood}

Description:
{prompt}

Requirements:

Studio quality.

Rich orchestration.

Balanced mix.

High fidelity.

Professional mastering.

Natural dynamics.

Immersive listening experience.

"""
        ).strip()