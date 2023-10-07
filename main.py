import Constants as keys
from  telegram.ext import *
import Responses as R

print("bot dimulai..")
# update.message.reply_text('Bot is ready')


def start_command(update, context):
    update.message.reply_text('type something random to get started')
    print("bot receipe")

def help_command(update, context):
    update.message.reply_text('if you need help, you should ask for it on google')
    print("bot receipe")

def handle_message(update, context):  #call to response
    text = str(update.message.text).lower()
    print("bot receipe", text)
    response = R.sample_responses(text)
    print("bot sendt")
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")



def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()







