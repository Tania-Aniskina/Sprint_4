class Locators:
    # Форма заказа первая страница "Для кого самокат"
    # Надпись "Для кого самокат"
    for_who_title = './/div[@class="Order_Content__bmtHS"]//div[text() = "Для кого самокат"]'
    # Поле "* Имя"
    name_field = './/input[@placeholder="* Имя"]'
    # Поле "* Фамилия"
    last_name_field = './/input[@placeholder="* Фамилия"]'
    # Поле "* Адрес: куда привезти заказ"
    address_field = './/input[@placeholder="* Адрес: куда привезти заказ"]'
    # Поле "* Станция метро"
    metro_station_field = './/input[@placeholder="* Станция метро"]'
    metro_first = 'select-search__row'
    # Поле "* Телефон: на него позвонит курьер"
    phone_field = './/input[@placeholder="* Телефон: на него позвонит курьер"]'
    # Кнопка "Далее"
    next_btn = './/button[text()="Далее"]'
    # Форма заказа вторая страница "Про аренду"
    # Надпись "Про аренду"
    about_rent_title = './/div[text()="Про аренду"]'
    # Поле "* Когда привезти самокат"
    when_bring_field = './/input[@placeholder="* Когда привезти самокат"]'
    # Поле "* Срок аренды"
    rent_time_field = './/div[@class = "Dropdown-control"]'
    rent_time_field_1_day = './/div[contains(@class, "Dropdown-option") and contains(text(), "сутки")]'
    rent_time_field_2_days = './/div[contains(@class, "Dropdown-option") and contains(text(), "двое суток")]'
    # Чек-бокс "Черный жемчуг"
    black_check_box = './/label[text()="чёрный жемчуг"]'
    # Чек-бокс "Серая безысходность"
    grey_check_box = './/label[text()="серая безысходность"]'
    # Поле "Комментарий для курьера"
    comment_field = './/input[@placeholder="Комментарий для курьера"]'
    # Кнопка "Заказать" в центре страницы
    order_on_body_btn = './/div[@class = "Order_Buttons__1xGrp"]//button[text()="Заказать"]'
    # Кнопка "Заказать" в header'е
    order_header_btn = './/div[@class = "Header_Nav__AGCXC"]//button[text() = "Заказать"]'
    # Надпись "Хотите оформить заказ?"
    want_to_finish_title = './/div[text()="Хотите оформить заказ?"]'
    # Кнопка "Да"
    yes_btn = './/button[text()="Да"]'
    # Надпись "Заказ оформлен"
    order_processed_title = './/div[text()="Заказ оформлен"]'
