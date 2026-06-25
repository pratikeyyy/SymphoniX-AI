"""
SymphoniX AI Theme
Luxury Black + Gold Theme
"""

import gradio as gr

APP_THEME = gr.themes.Base().set(

    # Backgrounds
    body_background_fill="#090909",

    block_background_fill="#151515",

    block_border_color="#2A2A2A",

    block_radius="20px",

    # Inputs
    input_background_fill="#101010",

    input_border_color="#2A2A2A",

    input_border_width="1px",

    # Text
    body_text_color="#FFFFFF",

    body_text_size="16px",

    block_title_text_color="#E8C547",

    block_label_text_color="#DDDDDD",

    # Buttons
    button_primary_background_fill="#C9A227",

    button_primary_background_fill_hover="#E0B92E",

    button_primary_border_color="#C9A227",

    button_primary_text_color="#000000",

    button_secondary_background_fill="#1A1A1A",

    button_secondary_border_color="#333333",

    button_secondary_text_color="#FFFFFF",

    # Links
    link_text_color="#E8C547",

    link_text_color_hover="#FFD95A",
)