from database.models import Card, User, Transaction
from database import get_db


# Добавить карту в базу
def add_user_card_to_db(**kwargs):
    db = next(get_db())
    card_number = kwargs.get('card_number')

    # Проверка была ли добавлена карта
    checker = db.query(Card).filter_by(card_number=card_number).first()

    if checker:
        return 'Карта есть в базе'

    new_card = Card
    db.add(new_card)
    db.commit()

    return 'Карта успешно добавлена'


# Сделать перевод с карты на карту
def transfer_money_db(card_from, card_to, date):
    pass


# Удалить карту из сервиса
def delete_user_card(card_id, user_id):
    pass


# Получить все карты по номеру телефона
def get_user_cards_by_phone_number_db(phone_number):
    pass


# Получить определенную карту
def get_exact_user_card(user_id, card_id):
    pass


# Получить все транзакции по определенной карте и по всем
def get_all_cards_or_exact_transactions(user_id, card_id):
    db = next(get_db())

    if card_id == 0:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id).all()


    else:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id, card_id=card_id).all()

    return card_monitor




