"""
SymphoniX AI
Premium Layout
"""

import gradio as gr


def custom_css():

    return """

    body{

        background:#090909;

    }

    .gradio-container{

        max-width:1500px !important;

        margin:auto;

        padding-top:20px;

    }

    footer{

        display:none;

    }

    .glass{

        background:rgba(20,20,20,.78);

        backdrop-filter:blur(20px);

        border:1px solid rgba(255,255,255,.08);

        border-radius:22px;

        padding:20px;

    }

    .hero-title{

        font-size:48px;

        font-weight:800;

        color:white;

    }

    .gold{

        color:#D4AF37;

    }

    .subtitle{

        color:#A5A5A5;

        font-size:17px;

        margin-top:8px;

    }

    .info-card{

        background:#131313;

        border-radius:18px;

        padding:18px;

        border:1px solid #2b2b2b;

    }

    .history{

        min-height:500px;

    }

    .music-card{

        min-height:350px;

    }

    """