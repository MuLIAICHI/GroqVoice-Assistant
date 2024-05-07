import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

load_dotenv()

filename = "output.wav"


def TTS(text):
    try:
        # STEP 1: Create the text 
        SPEAK_OPTIONS = {"text": text}
        # STEP 1: Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=os.getenv("DG_API_KEY"))

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        # STEP 3: Call the save method on the speak property
        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    TTS("Hello, how are you?")