from main import app
from database.cardservice import add_user_card_to_db, delete_user_card_db, get_user_cards_by_phone_number_db,\
    get_exact_user_card, get_all_cards_or_exact_transactions


# Добавления карты
@app.post('/add-user-card')
async def add_user_card_api(user_id: int, cardholder: str, card_name: str, card_number: int, exp_date: int, otp: int):
    result = add_user_card_to_db(user_id=user_id,
                                 cardholder=cardholder,
                                 card_name=card_name,
                                 card_number=card_number,
                                 exp_date=exp_date, otp=otp)

    return {"status": 1, "message": result}

# Генерация проверочного кода
@app.get('/one-time-password')
async def get_one_time_password(transfer_id: int):
    pass

# Перевод денег
@app.post('/transfer-user-money')
async def transfer_money_api(card_from: int, card_to: int, otp: int):
    pass

# Удаления карты
@app.delete('/delete-user-card')
async def delete_user_card(card_id: int, user_id: int):
    result = delete_user_card_db(card_id=card_id,
                                 user_id=user_id)

    return {"status": 1, "message": result}

# Получить карту
@app.get('/get-user-cards')
async def get_exact_or_all_cards(user_id: int, card: int = 0):
    if card == 0:
        cards = get_user_cards_by_phone_number_db(user_id)
    else:
        cards = get_exact_user_card(user_id, card)

    return {"status": 1, "cards": cards}


# Вывод истории карты
@app.get('/get-card-monitoring')
async def get_exact_all_card_monitoring(user_id: int, card: int = 0):
    card_monitoring = get_all_cards_or_exact_transactions(user_id, card)

    return {"status": 1, "card_monitoring": card_monitoring}


