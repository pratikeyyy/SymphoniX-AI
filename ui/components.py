"""
Reusable Components
"""

import gradio as gr


def hero():

    gr.HTML("""

<div style="

background:linear-gradient(135deg,#161616,#0A0A0A);

padding:35px;

border-radius:22px;

border:1px solid #2A2A2A;

margin-bottom:25px;

">

<h1 style="

font-size:46px;

margin:0;

color:white;

">

🎵 SymphoniX AI

</h1>

<p style="

font-size:18px;

color:#BBBBBB;

margin-top:12px;

">

Professional AI Music Studio

</p>

<p style="

color:#D4AF37;

font-size:15px;

">

Powered by Meta MusicGen • CUDA • Transformers

</p>

</div>

""")


def footer():

    gr.HTML("""

<div align="center"

style="

margin-top:25px;

color:#777777;

font-size:13px;

">

Made with ❤️ using

PyTorch • Transformers • Gradio

</div>

""")