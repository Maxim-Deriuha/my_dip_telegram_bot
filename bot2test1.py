import math
from telebot import types
import config
import telebot
import atb1
import skidki

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('unnamed.png', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Знижки АТБ")
    item2 = types.KeyboardButton("Знижки Посад")
    item3 = types.KeyboardButton("Знижки АТБ Газета")
    item4 = types.KeyboardButton("Знижки Велмарт")
    item5 = types.KeyboardButton("Знижки Фози")
    item6 = types.KeyboardButton("Знижки Сільпо")
    item7 = types.KeyboardButton("Знижки Рост")
    item8 = types.KeyboardButton("Автор")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    bot.send_message(message.chat.id,
                     "Ласкаво просимо , {0.first_name}!\nЯ бот - <b>{1.first_name}</b>,  створений для відображення  "
                     "знижок в продуктових магазинах. Будь-ласка виберіть потрібний магазин ".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    if message.chat.type == 'private':
        if message.text == 'Знижки АТБ':
            data = atb1.get_data()

            for product in data['products']:
                if float(product['old_price']) == 0.0:
                    product_message = product['title'] \
                                      + '\nНовий товар' \
                                      + '\nНова ціна : ' + product['price'] \
                                      + '\nЗнижка: '
                    sti = open('logo.png', 'rb')
                    bot.send_photo(message.chat.id, sti, product_message)
                else:
                    product_message = product['title'] \
                                      + '\nСтара ціна : ' + product['old_price'] \
                                      + '\nНова ціна : ' + product['price'] \
                                      + '\nЗнижка: ' + str(
                        math.trunc(float(product['old_price']) - float(product['price'])))
                    sti = open('logo.png', 'rb')
                    bot.send_photo(message.chat.id, sti, product_message)
        elif message.text == 'Знижки Посад':
            name_s = 'posad'
            index_posadmarket = skidki.get_skidki_index(name_s)
            posad_name = skidki.get_skidki_name(name_s)
            count = skidki.get_count_id(name_s)
            additional_info = skidki.get_additional_info(name_s)
            for k in range(count):
                for i in range(1, int(index_posadmarket[k]) + 1):
                    if i < 10:
                        skidki.picture_skidki(str(0) + str(i), posad_name[k])
                        product_message1 = additional_info[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
                    elif i > 10:
                        skidki.picture_skidki(i, posad_name[k])
                        product_message1 = additional_info[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
        elif message.text == 'Знижки АТБ Газета':
            name_s = 'atb'
            index_atb = skidki.get_skidki_index(name_s)
            name_atb = skidki.get_skidki_name(name_s)
            count_atb = skidki.get_count_id(name_s)
            additionalInfo_atb = skidki.get_additional_info(name_s)
            for k in range(count_atb):
                for i in range(1, int(index_atb[k]) + 1):
                    if i < 10:
                        skidki.picture_skidki(str(0) + str(i), name_atb[k])
                        product_message1 = additionalInfo_atb[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
                    elif i > 10:
                        skidki.picture_skidki(i, name_atb[k])
                        product_message1 = additionalInfo_atb[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)

        elif message.text == 'Знижки Велмарт':
            name_s = 'velmart'
            index_klass = skidki.get_skidki_index(name_s)
            klass_name = skidki.get_skidki_name(name_s)
            count_klass = skidki.get_count_id(name_s)
            additional_info_klass = skidki.get_additional_info(name_s)
            for k in range(count_klass):
                for i in range(1, int(index_klass[k]) + 1):
                    if i < 10:
                        skidki.picture_skidki(str(0) + str(i), klass_name[k])
                        product_message1 = additional_info_klass[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
                    elif i > 10:
                        skidki.picture_skidki(i, klass_name[k])
                        product_message1 = additional_info_klass[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
        elif message.text == 'Знижки Фози':
            name_s = 'fozzy'
            index_fozzy = skidki.get_skidki_index(name_s)
            fozzy_name = skidki.get_skidki_name(name_s)
            count_fozzy = skidki.get_count_id(name_s)
            additional_info_fozzy = skidki.get_additional_info(name_s)
            for k in range(count_fozzy):
                for i in range(1, int(index_fozzy[k]) + 1):
                    if i < 10:
                        skidki.picture_skidki(str(0) + str(i), fozzy_name[k])
                        product_message1 = additional_info_fozzy[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
                    elif i > 10:
                        skidki.picture_skidki(i, fozzy_name[k])
                        product_message1 = additional_info_fozzy[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)

        elif message.text == 'Знижки Сільпо':
            name_s = 'silpo'
            index_silpo = skidki.get_skidki_index(name_s)
            silpo_name = skidki.get_skidki_name(name_s)
            count_silpo = skidki.get_count_id(name_s)
            additional_info_silpo = skidki.get_additional_info(name_s)
            for k in range(count_silpo):
                for i in range(1, int(index_silpo[k]) + 1):
                    if i < 10:
                        skidki.picture_skidki(str(0) + str(i), silpo_name[k])
                        product_message1 = additional_info_silpo[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
                    elif i > 10:
                        skidki.picture_skidki(i, silpo_name[k])
                        product_message1 = additional_info_silpo[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)

        elif message.text == 'Знижки Рост':
            name_s = 'rost'
            index_rost = skidki.get_skidki_index(name_s)
            rost_name = skidki.get_skidki_name(name_s)
            count_rost = skidki.get_count_id(name_s)
            additional_info_rost = skidki.get_additional_info(name_s)
            for k in range(count_rost):
                for i in range(1, int(index_rost[k]) + 1):
                    if i < 10:
                        skidki.picture_skidki(str(0) + str(i), rost_name[k])
                        product_message1 = additional_info_rost[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)
                    elif i > 10:
                        skidki.picture_skidki(i, rost_name[k])
                        product_message1 = additional_info_rost[k]
                        sti = open('picture.png', 'rb')
                        bot.send_photo(message.chat.id, sti, product_message1)

        elif message.text == 'Автор':
            a = 'Дипломна робота Моніторинг знижок в продуктових магазинах \n' \
                    'Автор студент групи КІТ-117є  Дерюга М.В. \n' \
                    'Керівник Черних О.П. '
            sti = open('unnamed.png', 'rb')
            bot.send_photo(message.chat.id, sti, a)
        else:
            bot.send_message(message.chat.id,
                             "Нема такого варінту  ".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html')



if __name__ == '__main__':
    bot.infinity_polling()
