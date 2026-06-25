"""
============================================================
SymphoniX AI
Professional AI Music Studio
============================================================
"""

import time
import traceback
import gradio as gr

from services.music_service import MusicService
from ui.theme import APP_THEME
from ui.components import hero, footer


# ==========================================================
# Services
# ==========================================================

music_service = MusicService()


# ==========================================================
# CSS
# ==========================================================

CUSTOM_CSS = """
body {
    background: #090909;
}
.gradio-container {
    max-width: 1500px !important;
    margin: auto;
    padding: 25px;
}
footer {
    display: none;
}
.block {
    background: #141414;
    border: 1px solid #282828;
    border-radius: 20px;
}
.generate-btn {
    height: 55px;
    font-size: 18px;
    font-weight: 700;
}
.status-card {
    padding: 18px;
    border-radius: 18px;
    background: #121212;
    border: 1px solid #262626;
}
.track-card {
    padding: 20px;
    border-radius: 20px;
    background: #131313;
    border: 1px solid #262626;
}
"""


# ==========================================================
# Generate Function
# ==========================================================

def generate_music(prompt, genre, mood, duration):
    if not prompt.strip():
        raise gr.Error("Please enter a music prompt.")

    try:
        start = time.time()
        audio_path, generation_time = music_service.generate_music(
            prompt=prompt,
            genre=genre,
            mood=mood,
            duration=duration,
        )
        total = round(time.time() - start, 2)

        details = f"""
# ✅ Music Generated

### Prompt
{prompt}

---
🎼 Genre : **{genre}**
🎭 Mood : **{mood}**
⏱ Duration : **{duration} sec**
⚡ AI Generation : **{generation_time} sec**
🖥 Total Time : **{total} sec**

GPU : **CUDA**
Model : **Meta MusicGen**
"""
        return audio_path, details

    except Exception:
        traceback.print_exc()
        raise gr.Error("Music generation failed.")


# ==========================================================
# UI
# ==========================================================

with gr.Blocks(
    title="SymphoniX AI",
    theme=APP_THEME,
    css=CUSTOM_CSS,
) as demo:
    
    hero()

    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("## 🎼 Create Music")
            
            prompt = gr.Textbox(
                label="Prompt",
                lines=6,
                placeholder="Epic cinematic trailer with orchestra and powerful drums",
            )
            
            genre = gr.Dropdown(
                [
                    "Cinematic", "Lo-Fi", "Rock", "Pop", 
                    "EDM", "Jazz", "Ambient", "Classical"
                ],
                value="Cinematic",
                label="Genre",
            )
            
            mood = gr.Dropdown(
                [
                    "Epic", "Happy", "Sad", 
                    "Dark", "Energetic", "Relaxing"
                ],
                value="Epic",
                label="Mood",
            )
            
            duration = gr.Slider(
                minimum=5,
                maximum=30,
                value=10,
                step=5,
                label="Duration (Seconds)",
            )
            
            generate_btn = gr.Button(
                "🎵 Generate Music",
                variant="primary",
                elem_classes=["generate-btn"],
            )

        with gr.Column(scale=3):
            gr.Markdown("## 🎧 Generated Track")
            
            audio = gr.Audio(
                type="filepath",
                label="Music",
            )
            info = gr.Markdown()

    footer()

    # ==========================================================
    # Events (Now properly indented inside the `with gr.Blocks():` context)
    # ==========================================================
    generate_btn.click(
        fn=generate_music,
        inputs=[
            prompt,
            genre,
            mood,
            duration,
        ],
        outputs=[
            audio,
            info,
        ],
    )


# ==========================================================
# Launch
# ==========================================================

if __name__ == "__main__":
    demo.queue(max_size=10)
    demo.launch(
        server_name="127.0.0.1",
        show_error=True,
        inbrowser=True,
    )