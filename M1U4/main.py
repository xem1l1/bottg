
import telebot
import random   
import os 
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7937477480:AAEjro0A8YMVKoapGeZYtrT0i37TFA1xZeo")
memes = os.listdir("./img")    
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
     bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
 # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['mem','memes'])
def mem(message):
     
     global memes 
     words =  message.text.split()
     if len(words) > 1:
          number_mem = words[1] - 1
          if 0 <= number_mem < len(number_mem):
               with open(f"./img/{random.choice(memes)}","rb") as f:
                    return bot.send_photo(message.chat.id,f)
          else:
               return bot.send_message(message.chat.id,"мема с таким номерорм нет")

     r_mem = random.choice(memes)
     with open(f"./img/{random.choice(memes)}","rb") as f:
          bot.send_photo(message.chat.id,f)
     memes.remove(r_mem)
     if memes == []:
          memes = os.listdir("./img")
          
          

@bot.message_handler(commands=['calc'])  
def calc(message):
     words =  message.text.split()
     if len(words) > 2:
          if words[1] == "summa":
               number = int(words[2])
               summa = 0
               if number < 0:
                    for i in range(0, number - 1, -1):
                         summa += i 
               elif number > 0:
                    for i in range(0, number + 1):
                         summa += i 
               else:
                    summa = 0
               bot.reply_to(message, f'сумма всех чисел от 0 до {number} составила {summa}!')
          else:
               if len(words) == 4:
                    number1 = words [1]
                    number2 = words [3]
                    simbol = words [2]
                    result = 0
                    if simbol == "+":
                         result = number1 + number2
                    elif simbol == "-":
                         result = number1 - number2
                    elif simbol == "*":
                         result = number1 * number2
                    elif simbol == "/":
                         if number2 != 0:
                            result = number1 / number2
                         else:
                          result = "нельзя делить на ноль"
                    bot.reply_to(message, f'результат   {result} !')

@bot.message_handler(commands=['harm'])
def send_harm_info(message):
    harm_text = (
        "🐢 Пластик убивает морских черепах — они путают пакеты с медузами.\n"
        "🦅 Птицы глотают мусор и умирают от голода.\n"
        "🐬Дельфины и рыбы запутываются в сетках и пластиковых кольцах.\n"
        "🦊На суше животные могут пораниться об стекло или съесть пластик.\n\n"
        "⚠️Мусор — опасность для всех животных!"
    )
    bot.send_message(message.chat.id, harm_text) 

user_waiting_for_material = {}

@bot.message_handler(commands=['recycle'])
def send_recycle_info(message):
    chat_id = message.chat.id
    user_waiting_for_material[chat_id] = True
    bot.send_message(chat_id, "Что именно ты хочешь переработать? (например: пластик, стекло, бумага, батарейки)")

@bot.message_handler(func=lambda message: message.chat.id in user_waiting_for_material and user_waiting_for_material[message.chat.id])
def handle_recycle_item(message):
    chat_id = message.chat.id
    text = message.text.lower().strip()
    user_waiting_for_material.pop(chat_id)

    if "пластик" in text:
        bot.send_message(chat_id, "✅ Пластик нужно промыть и сдать отдельно. Упаковка с остатками еды не подходит.")
    elif "стекло" in text:
        bot.send_message(chat_id, "✅ Стекло нужно промыть. Крышки снять. Цветное и прозрачное стекло — отдельно.")
    elif "бумага" in text:
        bot.send_message(chat_id, "✅ Бумага должна быть чистой и сухой. Жирную и мокрую бумагу переработать нельзя.")
    elif "батарейка" in text or "батарейки" in text:
        bot.send_message(chat_id, "✅ Батарейки нужно сдавать в специальные пункты приёма (в магазинах, ТЦ и т.п.).")
    else:
        bot.send_message(chat_id, "🤔 Я пока не знаю, как перерабатывать это. Попробуй: пластик, стекло, бумага или батарейки.")                   
                    


                  
               



# Запуск бота
bot.polling()