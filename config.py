"""
SymphoniX AI
Global Configuration
"""

from dataclasses import dataclass
import torch


@dataclass(frozen=True)
class AppConfig:

    # --------------------------------------------------
    # App
    # --------------------------------------------------

    APP_NAME = "SymphoniX AI"
    VERSION = "1.0.0"

    # --------------------------------------------------
    # AI
    # --------------------------------------------------

    MODEL_NAME = "facebook/musicgen-small"

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # --------------------------------------------------
    # Music Generation
    # --------------------------------------------------

    DEFAULT_DURATION = 10

    MIN_DURATION = 5

    MAX_DURATION = 30

    DEFAULT_GENRE = "Cinematic"

    DEFAULT_MOOD = "Epic"

    MAX_NEW_TOKENS = 512

    # --------------------------------------------------
    # Paths
    # --------------------------------------------------

    GENERATED_FOLDER = "generated"

    LOG_FOLDER = "logs"

    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    THEME = "soft"

    TITLE = "🎵 SymphoniX AI"

    SUBTITLE = "Professional AI Music Generation Studio"