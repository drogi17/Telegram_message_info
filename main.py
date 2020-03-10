import telebot
import os

api_key = os.environ.get('API_KEY')
bot     = telebot.TeleBot(api_key)

@bot.message_handler(content_types=['text'])
@bot.message_handler(content_types=['sticker'])
@bot.message_handler(content_types=['file'])
@bot.message_handler(content_types=['photo'])
def message_reade(message):
    data    = 'User id: `%s`\n' % (message.from_user.id)
    data   += 'First name: `%s`\n' % (message.from_user.first_name, )
    data   += 'Last name: `%s`\n' % (message.from_user.last_name, )
    data   += 'Username: `%s`\n' % (message.from_user.username, )
    data   += 'Is bot: `%s`\n' % (message.from_user.is_bot, )
    data   += 'Link: [%s](%s)  (only works on phones)\n' % (message.from_user.username, 'tg://openmessage?user_id=' + str(message.from_user.id))
    data   += 'Text: `%s`\n' % (message.text)
    if message.forward_from:
        data   += '\n\n                  ** FORWARD FROM: **\n\n'
        data   += 'User id: `%s`\n' % (message.forward_from.id)
        data   += 'First name: `%s`\n' % (message.forward_from.first_name, )
        data   += 'Last name: `%s`\n' % (message.forward_from.last_name, )
        data   += 'Username: `%s`\n' % (message.forward_from.username, )
        data   += 'Is bot: `%s`\n' % (message.forward_from.is_bot, )
        data   += 'Link: [%s](%s)  (only works on phones)\n' % (message.forward_from.username, 'tg://openmessage?user_id=' + str(message.forward_from.id))
        # data   += 'Text: `%s`\n' % (message.text)
    if message.sticker:
        data   += '\n\n                  ** STICKER DATA: **\n\n'
        data   += 'Sticker id: `%s`\n' % (message.sticker.file_id)
        data   += 'Emoji: `%s`\n' % (message.sticker.emoji, )
        data   += 'Pack: [%s](https://t.me/addstickers/%s)\n' % (message.sticker.set_name, message.sticker.set_name)

    bot.send_message(message.chat.id, data, parse_mode="Markdown")
    # print(message)

print('started')
bot.polling()
