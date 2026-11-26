
import ollama


MODEL_NAME = "llama3.2"   #this is the llm I am using 

def ask_llm(messages):
    """messages: list of {"role": ..., "content": ...} dicts."""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={"num_predict": 80},  # replies are short, so cap the length
        keep_alive="30m",             # keep the model loaded between commands
    )
    reply = response["message"]["content"].strip()
    print(f"[LLM] Reply: \"{reply}\"")
    return reply

