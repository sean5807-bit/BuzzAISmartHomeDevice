from stt_whisper import listen_and_transcribe
from llm_ollama import ask_llm
from voice_helpers import buildPrompt, parseTask
import WeatherAPI

history = []

# task word from the AI  ->  function to call
TASKS = {
    "WEATHER": WeatherAPI.TodayWeather,
}

print("Buzz is ready. Press Ctrl+C to stop.")

while True:
    # 1. Listen
    heardText = listen_and_transcribe()
    if heardText == "":
        continue

    # 2. Ask the AI which task it is
    reply = ask_llm(buildPrompt(history, heardText))
    history.append({"role": "user", "content": heardText})
    history.append({"role": "assistant", "content": reply})

    # 3. Read the reply
    task, values = parseTask(reply)

    # 4. Call the right file, or use the CHAT answer
    if task in TASKS:
        data = TASKS[task](*values)
        print("Data:", data)
        answer = ask_llm([
            {"role": "system", "content": "Answer the question in one short sentence using only the data."},
            {"role": "user", "content": f"Question: {heardText}\nData: {data}"},
        ])
    else:
        answer = values[0]

    # 5. Output (later: speak it)
    print("Buzz:", answer)