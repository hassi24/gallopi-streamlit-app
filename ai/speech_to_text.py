import speech_recognition as sr
import tempfile

def transcribe_audio(audio_file):

    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as tmp:

        tmp.write(audio_file.read())
        path = tmp.name

    with sr.AudioFile(path) as source:

        audio = recognizer.record(source)

    try:

        text = recognizer.recognize_google(
            audio
        )

        return text

    except Exception:

        return ""