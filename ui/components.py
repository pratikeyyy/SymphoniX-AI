"""
Reusable Components
"""

import gradio as gr


def hero():

    gr.HTML("""

<style>

.hero{

position:relative;

overflow:hidden;

padding:45px;

border-radius:28px;

background:linear-gradient(135deg,#151515,#090909);

border:1px solid rgba(212,175,55,.18);

box-shadow:0 0 40px rgba(212,175,55,.08);

margin-bottom:25px;

}

.hero:before{

content:'';

position:absolute;

width:380px;

height:380px;

background:#D4AF37;

filter:blur(140px);

opacity:.08;

left:-120px;

top:-120px;

animation:move1 8s infinite alternate;

}

.hero:after{

content:'';

position:absolute;

width:320px;

height:320px;

background:#FFD95A;

filter:blur(120px);

opacity:.06;

right:-80px;

bottom:-120px;

animation:move2 10s infinite alternate;

}

@keyframes move1{

from{transform:translateX(0);}

to{transform:translateX(120px);}

}

@keyframes move2{

from{transform:translateY(0);}

to{transform:translateY(-120px);}

}

.logo{

font-size:58px;

font-weight:900;

color:white;

margin:0;

}

.gold{

color:#D4AF37;

}

.subtitle{

margin-top:15px;

font-size:18px;

color:#BEBEBE;

}

.row{

display:flex;

gap:18px;

margin-top:30px;

flex-wrap:wrap;

}

.card{

flex:1;

min-width:170px;

padding:18px;

background:rgba(255,255,255,.03);

border:1px solid rgba(212,175,55,.12);

border-radius:18px;

backdrop-filter:blur(15px);

transition:.3s;

}

.card:hover{

transform:translateY(-5px);

box-shadow:0 0 25px rgba(212,175,55,.2);

border-color:#D4AF37;

}

.value{

font-size:24px;

font-weight:800;

color:white;

}

.label{

font-size:13px;

color:#BDBDBD;

margin-top:5px;

}

</style>

<div class="hero">

<h1 class="logo">

🎵 Symphoni<span class="gold">X</span> AI

</h1>

<div class="subtitle">

Professional AI Music Generation Studio

</div>

<div style="margin-top:8px;color:#D4AF37;font-size:15px;">

Meta MusicGen • CUDA • Transformers • RTX Ready

</div>

<div class="row">

<div class="card">

<div class="value">⚡ CUDA</div>

<div class="label">GPU Acceleration</div>

</div>

<div class="card">

<div class="value">🎼 MusicGen</div>

<div class="label">Meta AI Model</div>

</div>

<div class="card">

<div class="value">🚀 Fast</div>

<div class="label">AI Music Generation</div>

</div>

<div class="card">

<div class="value">🎧 Studio</div>

<div class="label">Professional Quality</div>

</div>

</div>

</div>

""")
    

def footer():

    gr.HTML("""

<div align="center"

style="

margin-top:30px;

padding:20px;

color:#8F8F8F;

font-size:14px;

border-top:1px solid rgba(212,175,55,.15);

">

Made with ❤️ using <b>PyTorch</b> • <b>Transformers</b> • <b>Gradio</b>

</div>

""")
