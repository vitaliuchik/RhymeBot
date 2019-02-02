from scripts import constants, huificator, parsing
from telegram.ext import Updater, CommandHandler


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi! I'm a rhyme bot. (print /help)")


def bot_help(bot, update):
    message = """
    Commands:
    /rhymes word : prints rhymes for word (russian)
    /hui word : changes and prints word using huificator (recommended ukr words)
    """
    bot.send_message(chat_id=update.message.chat_id, text=message)


def rhymes(bot, update, args):
    rhymes_str = '\n'.join(parsing.get_rhymes(args[0]))
    bot.send_message(chat_id=update.message.chat_id, text=rhymes_str)


def hui(bot, update, args):
    hui_str = huificator.get_hui(args[0])
    bot.send_message(chat_id=update.message.chat_id, text=hui_str)


if __name__ == '__main__':
    updater = Updater(token=constants.TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler('help', bot_help)
    dispatcher.add_handler(help_handler)

    rhymes_handler = CommandHandler('rhymes', rhymes, pass_args=True)
    dispatcher.add_handler(rhymes_handler)

    huificator_handler = CommandHandler('hui', hui, pass_args=True)
    dispatcher.add_handler(huificator_handler)

    updater.start_polling()