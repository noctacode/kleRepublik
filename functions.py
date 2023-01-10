import configparser
import seleniumConfig
from ast import literal_eval
from itertools import islice
from random import uniform as random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import time
from variables import *

def browser_login():
    browser.find_element('id', 'citizen_email').send_keys(email)
    browser.find_element('id', 'citizen_password').send_keys(password)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    print('Logged in. (with password)')

def browser_login_sequence():    
    browser.get(url)
    cookies_set()
    browser.get(url)
    sleep(0.5)
    try: browser.find_element('id', 'citizen_email')
    except: print('Logged in. (with cookies)')
    else:
        browser_login()
        cookies_save()

def browser_popup_close():
    try: browser.find_element('xpath', '//*[@id="ErpkPopupPromosControllerPopup"]/a').click()
    except: return True

def browser_start():
    print('Opening browser.')
    global browser
    browser = seleniumConfig.browser()
    print('Browser opened.')

def config_read():
    global email
    global password
    global url

    config = configparser.ConfigParser()
    config.read('config.ini')

    email = config['user']['email']
    password = config['user']['password']

    url = config['default']['url']
    if url[-1] == '/': url = url[:-1]
        
def cookies_save():
    open('cookies', 'w')
    with open('cookies', 'a') as cookies_file:
        for cookie in browser.get_cookies():
            cookies_file.writelines(str(cookie)+'\n')
    print('Cookies saved.')

def cookies_set():
    browser.delete_all_cookies()
    with open('cookies') as cookies_file:
        for cookie in cookies_file:
            browser.add_cookie(eval(cookie))
    print('Cookies set.')

def money_change_check():
    browser.refresh()
    global money
    global money_old
    try: browser.find_element(By.CLASS_NAME, 'user_finances')
    except: browser.get('https://www.erepublik.com/en/economy/inventory')
    money_old['cc'] = money['cc']
    money_get()
    if money_old['cc'] == money['cc']:
        print()
        print('No changes.')
        return False
    else: return True

def money_get():
    global money
    money['g']=round(float(browser.find_element('id', 'side_bar_gold_account_value').get_attribute('data-amount')), 2)
    money['cc']=round(float(browser.find_element('id', 'side_bar_currency_account_value').get_attribute('data-amount')), 2)
    print('Gold:' + ' ' * (len(str(money['cc'])) - len(str(money['g']))), money['g'])
    print('Cash:', money['cc'])

def offers_compare():
    print('Comparing offers..')
    global offers_list_duplicates
    global offers_list_got
    global offers_list_modified
    global offers_list_new
    global offers_list_read    

    if not money_change_check(): return
    
    print()
    offers_get()
    offers_read()
    sleep(1)

    offers_compare_modified()
    offers_list_modified_length = offers_counter(offers_list_modified)
    if not offers_list_modified_length: print('No closed offers.')
    else:
        print()
        print('Offers closed:', offers_list_modified_length)
        offers_list_print(offers_list_modified)
    sleep(1)

    offers_compare_new()
    offers_list_new_length = offers_counter(offers_list_new)
    if not offers_list_new_length: print('No new offers.')
    else:
        print()
        print('Offers opened:', offers_list_new_length)
        offers_list_print(offers_list_new)

def offers_compare_duplicate():
    global offers_list_duplicates
    
    for tradeable in tradeables:
        offers_list_duplicates[tradeable] = []

    for tradeable in tradeables:
        offers_list_duplicates[tradeable] = [offer for offer in offers_list_got[tradeable] if offer in offers_list_read[tradeable]]

def offers_compare_forced():
    global money
    money['cc'] = -1
    offers_compare()

def offers_compare_modified():
    global offers_list_modified
    
    for tradeable in tradeables:
        offers_list_modified[tradeable] = []

    for tradeable in tradeables:
        offers_list_modified[tradeable] = [offer for offer in offers_list_read[tradeable] if offer not in offers_list_got[tradeable]]

def offers_compare_new():
    global offers_list_new
    
    for tradeable in tradeables:
        offers_list_new[tradeable] = []

    for tradeable in tradeables:
        offers_list_new[tradeable] = [offer for offer in offers_list_got[tradeable] if offer[0] not in offers_list_read_id and offer not in offers_list_read[tradeable]]

def offers_counter(offers_list):
    offers_counter = 0
    for tradeable in tradeables:
        offers_counter += len(offers_list[tradeable])
    return offers_counter

def offers_countries_missing(offers_list = offers_list_got, tradeables_included = ['Q2F', 'Q7F', 'Q7W', 'Q1H', 'Q2H', 'Q5M', 'WRM'], countries_exclude = ['Bulgaria', 'Iran', 'Ireland', 'Norway', 'Romania', 'Spain', 'USA']):
    print('Countries missing:')
    countries_without_excluded = [country for country in countries if country not in countries_exclude]
    for tradeable in tradeables_included:
        print()
        print(tradeable + ':')
        countries_from_offers = [offer[4] for offer in offers_list[tradeable]]
        for country in [country for country in countries_without_excluded if country not in countries_from_offers]:
            print(country)

def offers_get():
    global offers_list_got

    for tradeable in tradeables:
        offers_list_got[tradeable] = []
        
    browser.get('https://www.erepublik.com/en/economy/inventory')
    sleep(1)
    offers = browser.find_elements(By.CSS_SELECTOR, 'tr')[3:]
    
    for offer in offers:
        id = int(offer.get_attribute('data-offer_id'))
        country = country_code_name[offer.get_attribute('data-country_id')]
        item_industry = offer.get_attribute('data-industry_id')
        item_quality = offer.get_attribute('data-quality')
        amount = int(offer.get_attribute('data-amount'))
        price = float(offer.get_attribute('data-price'))
        item = code_item[item_industry+'_'+item_quality]
        
        offers_list_got[item].append([id, item, amount, price, country])
        print('.', end='')
    print(' Done.')
    print('Offers got:', offers_counter(offers_list_got))

def offers_list_print(offers_list):
    for tradeable in tradeables:
        print(tradeable + ':')
        for offer in offers_list[tradeable]:
            print(offer)

def offers_modified():
    for item in offers_set:
        country_set_for = [i for i in country_set]
        for offer in offers_by_item(item):
            country_set_for.remove(offer[4])
            print(item, ':', country_set_for, sep='')

def offers_read():
    global offers_list_read
    global offers_list_read_id
    offers_list_read_id = []
    for tradeable in tradeables:
        offers_list_read[tradeable] = []
        with open('offers/'+tradeable, 'r') as offers_read:
            offers_list_read[tradeable] += [literal_eval(offer) for offer in offers_read]
            for offer in offers_read:
                offers_list_read_id += literal_eval(offer)[0]
    print('Offers read:', len(offers_list_read_id))

def offers_set_print():
    global offers_file
    global offers_set
    offer_set = []
    for offer in offers_file:
        if offer[1] not in offers_set:
            offers_set.append(offer[1])
    print('Offers set.', offers_set)

def offers_write():
    global tradeables
    global offers_list_read
    
    for tradeable in tradeables:
        open('offers/'+tradeable, 'w').close()

    offers_write_counter = 0
    for tradeable in tradeables:
        with open('offers/'+tradeable, 'a') as file:
            for offer in offers_list_got[tradeable]:
                file.write('%s\n' % offer)
                offers_write_counter += 1
                
    print('Offers saved:', offers_write_counter)

def standard_start():
    browser_start()
    config_read()
    browser_login_sequence()
    browser_popup_close()

def storage_get():
    if browser.current_url != 'https://www.erepublik.com/en/economy/inventory':
        browser.get('https://www.erepublik.com/en/economy/inventory')
    for item in dict(list(storage.items())[:-5]):
        try:
            storage[item] = browser.find_element('id', 'stock_'+item_code[item]).get_attribute('formatnumber').strip('%')
        except: True
        print('.', end='')
    for item in dict(list(storage.items())[-5:]):
        try: storage[item] = int(browser.find_element('xpath', '//*[@title="'+item_code[item]+'"]').text.replace(',',''))
        except: True
        print('.', end='')
    print(' Done.')
    print('Storage read.')    

def storage_print():
    for item in storage:
        print(item,':',storage[item])
    
def wars_hunter_open(time_limit = 30, damage_limit_air = 25000, damage_limit_ground = 20000000):
    browser.get('https://erepublik.tools/en/military/battle-watcher/battle-heroes/11')
    sleep(5)
    wars = browser.find_elements(By.XPATH, '//*[@id="btabs-static-d11"]/ertools-battle-watcher-battle-heroes-overview/div/table/tbody/tr')
    for war in wars:
        damage = int(war.text.split(' ')[-2].replace(',', ''))
        time_left = int(war.text.split(' ')[-6].replace('min', ''))
        if time_left > time_limit + 1: break
        if damage < damage_limit_air + 1: 
            war.find_element(By.CSS_SELECTOR, 'a').click()
            print('!', end = '')
        else: print('.', end = '')
    print(' Air done.')

    browser.get('https://erepublik.tools/en/military/battle-watcher/battle-heroes/4')
    sleep(5)
    wars = browser.find_elements(By.XPATH, '//*[@id="btabs-static-d4"]/ertools-battle-watcher-battle-heroes-overview/div/table/tbody/tr')
    for war in wars:
        damage = int(war.text.split(' ')[-2].replace(',', ''))
        time_left = int(war.text.split(' ')[-7].replace('min', ''))
        if time_left > time_limit + 1: break
        if damage < damage_limit_ground + 1: 
            war.find_element(By.CSS_SELECTOR, 'a').click()
            print('!', end = '')
        else: print('.', end = '')
    print(' Ground done.')

def wars_paid_open():
    browser.get('https://www.erepublik.com/en/military/campaigns#search/combatOrders')
    sleep(1)

    try: browser.find_element(By.CLASS_NAME, 'showAll').click()
    except: True

    battle_cards = browser.find_elements(By.CLASS_NAME, 'war_card')
    for battle_card in battle_cards:
        if 'waiting' not in battle_card.text:
            browser.find_element(By.CLASS_NAME, 'fight_btn').send_keys(Keys.CONTROL, Keys.ENTER)
            sleep(random(1,8)) #longer delay to prevent pc lag

def wars_late_open():
    browser.get('https://www.erepublik.com/en/military/campaigns#search/lateBattle')
    sleep(1)
    
    try: browser.find_element(By.CLASS_NAME, 'showAll').click()
    except: True

    battle_cards = browser.find_elements(By.CLASS_NAME, 'war_card')
    for battle_card in battle_cards:
        if 'waiting' not in battle_card.text:
            browser.find_element(By.CLASS_NAME, 'fight_btn').send_keys(Keys.CONTROL, Keys.ENTER)
            sleep(random(1,8)) #longer delay to prevent pc lag
            
def variable_print(variable):
    print(eval(variable))

standard_start()
sleep(1)
print()
offers_compare()
print()
offers_countries_missing()
