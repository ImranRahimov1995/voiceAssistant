import pyaudio
from vosk import Model , KaldiRecognizer

from src.config import APP_DIR,ROOT_DIR,VOSK_MODEL_PATH


model = Model(VOSK_MODEL_PATH.__str__())
recognizer = KaldiRecognizer(model,16000)

_capture  = pyaudio.PyAudio()
stream = _capture.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8192,
)
stream.start_stream()

while True:
    data = stream.read(4096)
    if len(data) == 0:
        break

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())