import time

import Constants as keys
import Responses as R
from  telegram.ext import *

print("bot dimulai..")

for x in range(100):
    print("nilai X:",x)
    def start_command(update, context):
        update.message.reply_text('type something random to get started')
        print("bot receipe")

    def help_command(update, context):
        update.message.reply_text('if you need help, you should ask for it on google')
        print("bot receipe")

    def handle_message(update, context):  #call to response
        text = str(update.message.text).lower()
        print("bot receipe 1", text)
        if(text == '1'):
            for x in range(2):
                update.message.reply_text(x)
        else:
            response = R.sample_responses(text)
            print("bot sendt")
            update.message.reply_text(response)


    def sender_message(update, context):  #call to response
        text = str(update.message.text).lower()
        print("bot receipe 2", text)
        if(text == '2'):
            for x in range(3):
                update.message.reply_text(x)
        else:
            response = R.sample_responses(text)
            print("bot sendt")
            update.message.reply_text(response)


    def error(update, context):
        print(f"Update {update} caused error {context.error}")

    def kirim(a, b):
        print(f"update {a} caused {b}")



    def main():
        updater = Updater(keys.API_KEY, use_context=True)
        dp = updater.dispatcher

        print("bot receive chat")
        dp.add_handler(CommandHandler("start", start_command))
        print("1")
        dp.add_handler(CommandHandler("help", help_command))
        print("2")

        print(Filters.text)
        print(handle_message)
        dp.add_handler(MessageHandler(Filters.text, handle_message))
        print("3")

        dp.add_error_handler(error)
        print("4")

        updater.start_polling()
        print("5")
        updater.idle()
        print("6")

    a = 'b'
    if (a=='b'):
        print("ayooooo")
        kirim(1, 2)

    main()







