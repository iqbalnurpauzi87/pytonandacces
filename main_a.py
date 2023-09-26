import Constants as keys
from  telegram.ext import *
import Responses as R

print("bot dimulai..")

def start_command(update, context):
    update.message.reply_text('type something random to get started')

def help_comman(update, context):
    update.message.reply_text("if you need help, you should ask for it on google")

def handle_comman(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} cause error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcer

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))


    dp.add_handler(MessagedHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()

main()







