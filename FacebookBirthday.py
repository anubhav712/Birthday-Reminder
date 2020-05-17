from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# time module to wait for it to execute after sometime
import time
import sys

# password module
import getpass

url = "https://www.facebook.com/events"


def __login(driver, user, password):

    try:
        driver.get(url)
        element = driver.find_element_by_id("email")
        element.send_keys(user)
        element = driver.find_element_by_id("pass")
        element.send_keys(password)    
        print('Attempting logging with your credentials')

        element.send_keys(Keys.RETURN)
        time.sleep(10)
        return True

    except Exception as exception:
        print(exception)
        return False


def __create_driver(path_to_driver):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(path_to_driver, options=chrome_options)
    return driver


def birthdays(user, password, choice, path_to_driver):
    driver = __create_driver(path_to_driver)

    if(__login(driver, user, password)):
        print('Logging Successfull\n')

        select = "//span[contains(text(),'Birthdays')]"
        driver.find_element_by_xpath(select).click()
        time.sleep(2)

        try:
            birthday_path = './/h2[contains(text(),'+__generate_birthday_type(
                                choice)+')]/ancestor::div[2]/child::div[2]'
            find_parent = driver.find_element(By.XPATH, birthday_path)

            birthday_tags = find_parent.find_elements(By.XPATH, "./div")

            print(str(len(birthday_tags))+' of your friends have birthday\n ')
            for i in birthday_tags:
                try:
                    names = i.find_element(By.TAG_NAME, "h2")
                    print(names.text)
                except Exception as e:
                    print(e)
                    pass

        except NoSuchElementException:
            print('None of your friends birthday')
            pass
        finally:
            driver.close()
            print('\nDone')

    else:
        print("Login Un-successfull")


def __generate_birthday_type(choice):
    if(choice == '1' or choice == ''):
        return '"Today\'s Birthdays"'
    elif choice == '2':
        return '"Upcoming Birthdays"'
    else:
        return '"Recent Birthdays"'


def get_user_input():
    user = input('Enter your email: ')
    password = getpass.getpass('Enter your passowrd:')
    choice = input("\n\nChoose Birthday Type\n1 Today Birthdays\n2 Upcoming" +
                   " Birthdays\n3 Recent Brithdays\nEnter number ")
    return user, password, choice


if(__name__ == '__main__'):

    user_details = get_user_input()
    birthdays(user_details[0], user_details[1], user_details[2], sys.argv[1])
