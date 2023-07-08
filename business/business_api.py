from main import app


@app.post('/register-business-category')
async def register_business_category_api(name: str): 
    pass


@app.post('/register-business')
async def register_business(category_id: int, name: str, card_number: int): 
    pass

# Получить
@app.get('/get-all-categories')
async def get_business_categories_api(exact_category_id: int = 0): 
    pass

# Вывод услуг
@app.get('/get-business')
async def get_exact_business_api(business_id: int, category_id: int): 
    pass

# Оплата услуг
@app.get('/pay-service')
async def pay_for_service(business_id: int, from_card: int, amount: float): 
    pass

# Удалить бизнес
@app.delete('/delete-business')
async def delete_business_api(business_id: int): 
    pass













