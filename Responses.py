from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text),lower()

    if user_message in ("hello", "hi", "sup"):
        return "hey! How's it going"

    if user_message in ("who are you", "who are you?"):
        return "i am abc bot"

    if user_message in ("time"):
        now = datetime.now()
        datetime = nowstrftime("%d/%m/$y, %H:%M:%S")

        return str(datetime)

    return "I dont understand"