
# Token telegran bot
import code

bot_token = '5323958977:AAFOwR3lLw-bwBNoDiG5Y7tEialu2tZoax0' # токен бота
CHANNEL_ID = 1671513660 # id канала куда будет отсылаться информация, ид без -100 в начале (например: 124873248) - указать заместо нуля

# ID admin
admin_id = 263040074  # id админа - указать заместо нуля

bot_login = 'MURMUR_ONLINE_bot' # логин бота
ref_percent = 8 # Процент реферальной системы

QIWI_NUMBER = '+79528578483'    # номер киви
QIWI_TOKEN = '1572855df18da64ce7c54f7ebbde309b'            # токен киви

text_purchase = '❕ Вы выбрали: ' \
                '{name}\n\n' \
                '{info}\n\n' \
                '💠 Цена: {price} рублей\n' \
                '💠 Кол-во кладов: {amount}' \


# инфа
info = f''' ❗Если у вас возникла проблема с оплатой, пишите сюда: <b>@MURMUR_support_bot</b>\n
❓По всем остальным вопросам: <b>@EL_SUPPO</b>  
 \n'''

# Пополнение баланса qiwi
replenish_balance=f'➕ <b>Пополнение баланса\n\n</b>' \
                    '🥝 <u>Пополнение баланса через QIWI</u>: \n\n' \
                    '➖➖➖➖➖➖➖➖➖➖\n\n'\
                    f'📱 <b>Номер для оплаты:</b>' ' {number}\n' \
                    f'📋 <b>При переводе указать комментарий: </b>' '{code}\n\n' \
                    '➖➖➖➖➖➖➖➖➖➖\n\n'\
                    f'❗️Если у вас возникли какие-либо проблемы с пополнением обратитесь в поддержку и перешлите туда это сообщение или приложите комментарий.\n\n' \
                    f'💵 <i>Сумма пополнения не должна превышать 15000 рублей</i>\n\n' \
                    f'После оплаты нажмите 🔄 Проверка оплаты'

# Пополнение баланса карта
card_balance=f'➕ <b>Пополнение баланса</b>\n\n' \
              f'💵 <u>Пополнение баланса через карту</u>\n\n' \
                '➖➖➖➖➖➖➖➖➖➖\n\n' \
                f'💳<b>Номер карты для пополнения:</b> <code>5536913884700341</code> \n\n' \
                '➖➖➖➖➖➖➖➖➖➖\n\n' \
                f'❗️Оплата принимается только на <b>НОМЕР БАНКОВСКОЙ КАРТЫ.</b> Пополнить банковскую карту можно любым удобным способом, например: со своего QIWI-кошелька, терминала, банковской карты (card2card), Yandex.Деньги, Payeer, WebMoney и другие платежные системы.\n\n' \
                f'Вопросы по зависшим платежам принимаются в течении суток с момента оплаты.\n\nЧто бы узнать статус пополнения обязательно пришлите в поддержку <b>ваш ID</b> (<i>указан в профиле</i>), <b>номер карты</b> на которую совершили пополнение и <b>точную сумму платежа!</b>\n'

# Пополнение баланса btc

renish_balance=f'➕ <b>Пополнение баланса</b>\n\n' \
                     f'🅱️ <u>Пополнение баланса через BTC</u> \n\n' \
                     '➖➖➖➖➖➖➖➖➖➖\n\n'\
                     f'<b>Номер счета для пополнения: </b><code>1CgqxCt3RTnXkEKX5EN9TUYVSrbUSGUotc</code>\n\n' \
                     f'🕐 Пополните счет в течении <b>60 мин.</b>\n\n' \
                     '➖➖➖➖➖➖➖➖➖➖\n\n'\
                     f'❗️<b>Внимание!</b> Заявка будет оплачена после 1-го подтверждения в сети Bitcoin (BTC) \n\n' \
                     f'♻️ <b>Статус:</b>  Количество подтверждений: 0️⃣ / 1️⃣\n\n' \
                     f'<i>Возможна задержка, так как операция проводится вручную.</i>\n\n' \



# Профиль
profile = f'🌐 <b>Профиль\n\n</b>' \
          '➖➖➖➖➖➖➖➖➖➖\n\n' \
          '👁‍🗨 <b>ID: </b> {id}\n' \
          '👤 <b>Логин: </b> {login}\n' \
          '📅 <b>Дата регистрации: </b> {data}\n\n' \
          '➖➖➖➖➖➖➖➖➖➖\n\n' \
          '💰 <b>Ваш баланс: </b>{balance} <b>рублей</b>'
