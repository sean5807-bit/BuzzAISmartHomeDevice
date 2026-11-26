"""
This file is going to help interperet what the ai spits out and determines which
file needs to run 
"""

MAX_HISTORY_MESSAGES = 6  # how many past messages Buzz remembers

#this is the prompt so far and needs to built on 
SYSTEM_PROMPT = """You are Buzz, a voice assistant. Decide what the user wants.
Reply with ONLY one line in this format:  TASK | value | detail
Do not add any other words.

Tasks:
WEATHER | <city> | <detail>
    Use for ANY weather question. If no city is given, use Atlanta.
    detail must be ONE of these words:
    TEMPERATURE, FEELSLIKE, HUMIDITY, PRECIPITATION, WIND, UV, ALL
    Use ALL if they ask about the weather in general.
CHAT | <your short answer>
    Use for anything that is not about weather.

Examples:
User: what's the weather in New York
You: WEATHER | New York | ALL
User: how humid is it in Atlanta
You: WEATHER | Atlanta | HUMIDITY
User: is it going to rain
You: WEATHER | Atlanta | PRECIPITATION
User: how windy is it in Chicago
You: WEATHER | Chicago | WIND
User: what does it feel like outside
You: WEATHER | Atlanta | FEELSLIKE
User: is it sunny in Miami
You: WEATHER | Miami | CONDITION
User: how hot is it
You: WEATHER | Atlanta | TEMPERATURE
User: what's two plus two
You: CHAT | Two plus two is four.
"""

def buildPrompt(history, heardText):
    messages = []
    messages.append({"role": "system", "content": SYSTEM_PROMPT})
    for hist in history[-MAX_HISTORY_MESSAGES:]:  # only the most recent messages
        messages.append(hist)
    messages.append({"role": "user", "content": heardText})
    return messages



def parseTask(reply): #goes through response from ai to return a value
    if "|" not in reply:          # AI ignored the format, so treat it as a normal answer
        return ("CHAT", [reply])

    splitReply = reply.split("|")
    fileCall = splitReply[0].strip().upper()
    city = "Atlanta" # assumes atlanta if ai left the city out 
    task = "ALL" #another assumptions 
    if fileCall == "WEATHER":
        if len(splitReply) > 1:
            city = splitReply[1].strip()
        if len(splitReply) > 2:
            task = splitReply[2].strip().upper()
        return (fileCall, [city, task])
    # can add more options later on 

    return ("CHAT", [splitReply[1].strip()])
    