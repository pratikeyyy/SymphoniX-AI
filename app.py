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
/* ===========================
   GLOBAL
=========================== */

body{
    background:linear-gradient(-45deg,#090909,#111111,#171717,#090909);
    background-size:400% 400%;
    animation:bgMove 18s ease infinite;
    font-family:Inter,sans-serif;
}

@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.gradio-container{
    background:#090909 !important;
    background-image:
    radial-gradient(circle at top left,#D4AF3720 0%,transparent 35%),
    radial-gradient(circle at bottom right,#FFD95A15 0%,transparent 30%);
    min-height:100vh;
}

.gr-block{
    background:#141414 !important;
    border:1px solid #D4AF3730 !important;
    border-radius:22px !important;
    transition:.3s;
}

.gr-block:hover{
    transform:translateY(-4px);
    border-color:#D4AF37 !important;
    box-shadow:0 0 25px rgba(212,175,55,.2);
}

.gr-button-primary{
    background:linear-gradient(90deg,#D4AF37,#FFD95A)!important;
    color:#000!important;
    border:none!important;
    border-radius:18px!important;
}

.gr-button-primary:hover{
    transform:scale(1.03);
    box-shadow:0 0 25px rgba(212,175,55,.4);
}

.gr-textbox textarea,
.gr-textbox input{
    background:#111!important;
    color:white!important;
    border:1px solid #333!important;
}

.gr-dropdown{
    background:#111!important;
}

.gr-slider input{
    accent-color:#D4AF37;
}
footer{
    display:none !important;
}

/* ===========================
   ANIMATION
=========================== */

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

@keyframes glow{
    0%{
        box-shadow:0 0 0 rgba(212,175,55,0);
    }
    50%{
        box-shadow:0 0 30px rgba(212,175,55,.35);
    }
    100%{
        box-shadow:0 0 0 rgba(212,175,55,0);
    }
}

@keyframes float{
    0%{transform:translateY(0px);}
    50%{transform:translateY(-5px);}
    100%{transform:translateY(0px);}
}

/* ===========================
   CARDS
=========================== */

.block{

    background:rgba(20,20,20,.78)!important;

    backdrop-filter:blur(18px);

    border:1px solid rgba(212,175,55,.15)!important;

    border-radius:22px!important;

    transition:.35s ease;

    overflow:hidden;

}

.block:hover{

    transform:translateY(-5px);

    border-color:#D4AF37!important;

    box-shadow:0 0 30px rgba(212,175,55,.18);

}

/* ===========================
   BUTTON
=========================== */

.generate-btn{

    height:58px!important;

    font-size:18px!important;

    font-weight:700!important;

    border:none!important;

    border-radius:18px!important;

    color:#000!important;

    background:linear-gradient(90deg,#D4AF37,#FFD95A)!important;

    transition:.35s ease!important;

}

.generate-btn:hover{

    transform:scale(1.03);

    animation:glow 1.5s infinite;

}

/* ===========================
   INPUTS
=========================== */

textarea,
input,
select{

    background:#111!important;

    color:white!important;

    border:1px solid #333!important;

    border-radius:15px!important;

}

textarea:focus,
input:focus,
select:focus{

    border-color:#D4AF37!important;

    box-shadow:0 0 15px rgba(212,175,55,.25)!important;

}

/* ===========================
   LABELS
=========================== */

label{

    color:#E5E5E5!important;

    font-weight:600!important;

}

/* ===========================
   MARKDOWN
=========================== */

h1{

    color:white!important;

}

h2{

    color:#FFD95A!important;

}

h3{

    color:white!important;

}

p{

    color:#BDBDBD!important;

}

/* ===========================
   AUDIO
=========================== */

audio{

    width:100%;

    border-radius:18px;

    box-shadow:0 0 25px rgba(212,175,55,.18);

    animation:float 5s ease infinite;

}

/* ===========================
   STATUS CARD
=========================== */

.status-card{

    background:#141414;

    border-radius:18px;

    border:1px solid #2b2b2b;

    padding:20px;

}

/* ===========================
   TRACK CARD
=========================== */

.track-card{

    background:#131313;

    border-radius:20px;

    border:1px solid #2b2b2b;

    padding:20px;

}

/* ===========================
   SCROLLBAR
=========================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-track{

    background:#090909;

}

::-webkit-scrollbar-thumb{

    background:#D4AF37;

    border-radius:20px;

}

/* ===========================
   DROPDOWN
=========================== */

.gr-dropdown{

    border-radius:15px!important;

}

/* ===========================
   SLIDER
=========================== */

input[type=range]{

    accent-color:#D4AF37;

}

/* ===========================
   IMAGE / ICON HOVER
=========================== */

img{

    transition:.35s;

}

img:hover{

    transform:scale(1.05);

}

/* ===========================
   MOBILE
=========================== */

@media(max-width:900px){

.gradio-container{

padding:15px;

}

h1{

font-size:34px!important;

}

.generate-btn{

height:52px!important;

font-size:16px!important;

}

}
"""


# ==========================================================
# Generate Function
# ==========================================================

def generate_music(prompt, genre, mood, duration):

    if not prompt.strip():
        raise gr.Error("Please enter a music prompt.")

    try:

        yield (
            None,
            """
# ⚡ Initializing AI...

🟨□□□□□□□□□ 10%

Loading MusicGen...
""",
        )

        time.sleep(5)

        yield (
            None,
            """
# 🎼 Composing Melody...

🟨🟨🟨🟨□□□□□□ 40%

Building musical structure...
""",
        )

        time.sleep(5)

        yield (
            None,
            """
# 🥁 Generating Instruments...

🟨🟨🟨🟨🟨🟨🟨□□□ 75%

Creating drums, bass and harmony...
""",
        )

        start = time.time()

        audio_path, generation_time = music_service.generate_music(
            prompt=prompt,
            genre=genre,
            mood=mood,
            duration=duration,
        )

        total = round(time.time() - start, 2)

        yield (
            audio_path,
            f"""
# ✅ Music Generated Successfully

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
""",
        )

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
    show_progress="full",
)


# ==========================================================
# Launch
# ==========================================================

if __name__ == "__main__":
    demo.queue(max_size=10)
    demo.launch(
        share=True,
        server_name="127.0.0.1",
        show_error=True,
        inbrowser=True,
    )
