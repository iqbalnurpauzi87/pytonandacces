from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "hey! How's it going"

    if user_message in ("who are you", "who are you?"):
        return "i am abc bot"

    if user_message in ("hai cantik", ""):
        return "makasih ganteng"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    if user_message in ("p", ""):
        return "p p p terus berisik"

    return "I dont understand you"