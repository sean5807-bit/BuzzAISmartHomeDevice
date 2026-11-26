"""
stt_whisper.py
"""
import sys

import sounddevice as sd
import whisper

SAMPLE_RATE = 16000       # Whisper expects 16kHz mono audio
RECORD_SECONDS = 6        # how long we listen each time we ask for a command
#changed this because there wasn't enough time to talk
# This downloads the model once (to ~/.cache/whisper) and then reuses it.
print("[STT] Loading Whisper model (only happens once per run)...")
_model = whisper.load_model("base")
print("[STT] Whisper ready.")


def listen_and_transcribe():
    """
    Records RECORD_SECONDS of audio from the default microphone,
    transcribes it with Whisper, and returns the resulting text
    (empty string if nothing understandable was heard).
    """
    print(f"[STT] Listening for {RECORD_SECONDS} seconds... speak now.")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )
    sd.wait()  # block until recording finishes
    audio = audio.flatten()

    # fp16=False avoids a warning/slowdown on CPUs without fp16 support
    result = _model.transcribe(audio, fp16=False)
    text = result["text"].strip()

    if text:
        print(f"[STT] Heard: \"{text}\"")
    else:
        print("[STT] (didn't catch anything)")

    return text



if __name__ == "__main__":
    while True:
        request = sys.stdin.readline()
        if request == "":
            break  # main.py closed the pipe, so we shut down
        spoken_text = listen_and_transcribe()
        print("HEARD:" + spoken_text.replace("\n", " "), flush=True)
