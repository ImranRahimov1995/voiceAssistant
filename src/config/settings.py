from pathlib import Path


APP_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

VOSK_MODEL_PATH = ROOT_DIR / 'vosk_model'
