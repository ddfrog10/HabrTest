"""Локаторы на странице настройки профиля"""


class ProfileScreen:
    setting_profile = '//a[1]/span[@class="tm-user-menu__menu-link-text"]'
    profile = '//*[@data-test-id="tab-link-active"]'
    name_profile = '[name=fullname]'
    speciality_profile = '[name = speciality]'
    gender_profile = '[name = gender]'
    birthday_day = '[name=birthdayDay]'
    birthday_month = '[name=birthdayMonth]'
    birthday_year = '[name=birthdayYear]'
    location_country = '[name=locationCountryId]'
    location_region = '[name=locationRegionId]'
    location_city = '[name= locationCityId]'
    remove_contacts = '//*[@class="base-fieldset__remove  base-fieldset__remove_contacts "]'
    button_contacts = '//*[@class="base-button base-button__fieldset"]'
    contact_type = '[name=contactTypeId]'
    contact_value = '[name=contactValue]'
    payment_ym = '[name=paymentYandexMoney]'
    payment_pay_pal = '[name=paymentPayPalMe]'
    payment_webmoney = '[name=paymentWebmoney]'
    save_button = '//*[@type="submit"]'
    toast_success = '//*[@class="Vue-Toastification__toast Vue-Toastification__toast--success top-center"]'
