import telebot
import config
import FSM

from telebot import types

bot = telebot.TeleBot('5424461976:AAHoiCeR11iKtVNe22TbcL5v-4fFD6iLDG0')
fsm = FSM.TelegramBot()

@bot.message_handler(commands=['start'])
def welcome(message):

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказать пиццу")
    item2 = types.KeyboardButton("Посмотреть меню")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> бот, я помогу вам "
                     "сделать заказ.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
@bot.message_handler(func=lambda message: fsm.state == 'asleep')
def order_pizza(message):
    bot.send_message(message.chat.id, 'Какую вы хотите пиццу? Большую или маленькую?')
    fsm.asked_for_payment_method(message.text)




@bot.message_handler(content_types=['text'])
@bot.message_handler(func=lambda message: fsm.state == 'size_selected')
def choose_size(message):
    bot.send_message(message.chat.id, 'Как вы будете платить?')
    fsm.asked_for_payment_method(message.text)

@bot.message_handler(content_types=['text'])
@bot.message_handler(func=lambda message: fsm.state == 'payment_selected')
def choose_size(message):
    bot.send_message(message.chat.id, 'Какой вкус вы хотите?')
    fsm.asked_for_flavour(message.text)
@bot.message_handler(content_types=['text'])
@bot.message_handler(func=lambda message: fsm.state == 'flavour_selected')
def choose_size(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да", callback_data='yes')
    item2 = types.InlineKeyboardButton("Нет ", callback_data='no')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, f'Вы хотите {fsm.size} пиццу {fsm.flavour}, оплата - {fsm.pay_method} ?', reply_markup=markup)





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'Спасибо за заказ')
                fsm.confirmed()
                # show alert
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text="Заказ оформлен")
            elif call.data == 'no':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Заказать пиццу")
                item2 = types.KeyboardButton("Посмотреть меню")

                markup.add(item1, item2)

                bot.send_message(call.message.chat.id, 'Бывает 😢', reply_markup=markup)
                fsm.confirmed()

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Вы хотите {fsm.size} пицца {fsm.flavour}, оплата - {fsm.pay_method} ?',
                                  reply_markup=None)



    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)