from pathlib import Path


APP_DIR = Path(__file__).resolve().parent
ROOT_DIR = Path(__file__).resolve().parent.parent

VOSK_MODEL_PATH = APP_DIR / 'vosk_model'
